#!/usr/bin/env python3
"""Run the xshi-math GPT-5.5 pro deep math consultant.

The script prepares a bounded context package for a direct OpenAI Responses API
run when no hosted tools are needed, falling back to the OpenAI Agents SDK for
web search or hosted file search. Text files are inlined, PDFs are uploaded as
file inputs, and images are sent as vision inputs. Use --dry-run to inspect the
package without making an API call.
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import sys
import textwrap
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


DEFAULT_MODEL = "gpt-5.5-pro"
DEFAULT_REASONING_EFFORT = "xhigh"
DEFAULT_MAX_OUTPUT_TOKENS = 100_000
DEFAULT_MAX_POLL_SECONDS = 3600.0
DEFAULT_POLL_INTERVAL_SECONDS = 10.0
DEFAULT_CONTEXT = (
    "AGENTS.md",
    "docs/rules/mathematical-writing.md",
    "docs/rules/shared-notation.md",
    "content/notation.md",
)
TEXT_EXTENSIONS = {
    ".bib",
    ".cfg",
    ".csv",
    ".ipynb",
    ".json",
    ".md",
    ".py",
    ".rst",
    ".tex",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
IMAGE_EXTENSIONS = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
SKIP_DIRS = {
    ".git",
    ".ipynb_checkpoints",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "_build",
    "build",
    "dist",
    "node_modules",
    "venv",
}
PENDING_RESPONSE_STATUSES = {"queued", "in_progress"}
SUCCESS_RESPONSE_STATUS = "completed"


AGENT_INSTRUCTIONS = """\
You are the xshi-math deep math research consultant.

Your job is to produce a rigorous Markdown report for Codex, not to edit files.
Focus on fat tails, extreme value theory, probability, statistics, decision
theory, information geometry, mixture models, and mathematical exposition
across the Incerto, IG, and Normix-theory tracks.

Ground claims in the supplied repository context, attached PDFs or figures,
primary sources found through web search, computations, or explicit caveats.
Use the project's notation when it is supplied. State assumptions visibly.
Paraphrase copyrighted material instead of reproducing it. If a proof is not
complete, say exactly where the gap is and propose verification steps.

Do not reveal hidden chain-of-thought. Provide concise derivations, proof
sketches, examples, counterexamples, and audit trails that Codex can verify.
Return Markdown only, following the requested report contract.
"""


@dataclass(frozen=True)
class ContextPackage:
    inline_sections: list[str]
    inline_paths: list[Path]
    pdf_paths: list[Path]
    image_paths: list[Path]
    skipped: list[str]


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a GPT-5.5 pro OpenAI consultant for xshi-math work."
    )
    prompt_group = parser.add_mutually_exclusive_group(required=True)
    prompt_group.add_argument("--prompt", help="Research request to send to the agent.")
    prompt_group.add_argument(
        "--prompt-file",
        type=Path,
        help="Path to a UTF-8 text file containing the research request.",
    )
    parser.add_argument(
        "--context",
        action="append",
        default=[],
        type=Path,
        help="File or directory to include. May be repeated.",
    )
    parser.add_argument(
        "--context-glob",
        action="append",
        default=[],
        help="Glob relative to --repo-root selecting additional context files.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Repository root used for relative paths. Defaults to cwd.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional Markdown output path. The report is printed to stdout either way.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("XSHI_MATH_DEEP_MATH_MODEL", DEFAULT_MODEL),
        help=f"OpenAI model to use. Defaults to {DEFAULT_MODEL}.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=("none", "minimal", "low", "medium", "high", "xhigh"),
        default=os.environ.get(
            "XSHI_MATH_DEEP_MATH_REASONING_EFFORT", DEFAULT_REASONING_EFFORT
        ),
        help=f"Reasoning effort. Defaults to {DEFAULT_REASONING_EFFORT}.",
    )
    parser.add_argument(
        "--verbosity",
        choices=("low", "medium", "high"),
        default=os.environ.get("XSHI_MATH_DEEP_MATH_VERBOSITY", "high"),
        help="Model verbosity setting.",
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=int(
            os.environ.get(
                "XSHI_MATH_DEEP_MATH_MAX_OUTPUT_TOKENS",
                str(DEFAULT_MAX_OUTPUT_TOKENS),
            )
        ),
        help=(
            "Maximum output tokens requested from the model, including visible "
            "output and reasoning tokens."
        ),
    )
    parser.add_argument(
        "--max-inline-kb",
        type=int,
        default=256,
        help="Maximum text per inlined file before truncation.",
    )
    parser.add_argument(
        "--max-attachment-mb",
        type=int,
        default=64,
        help="Maximum PDF or image file size to attach.",
    )
    parser.add_argument(
        "--no-default-context",
        action="store_true",
        help="Do not automatically include AGENTS.md, writing/notation rules, and content/notation.md.",
    )
    parser.add_argument(
        "--no-web-search",
        action="store_true",
        help="Disable hosted web search.",
    )
    parser.add_argument(
        "--vector-store-id",
        action="append",
        default=[],
        help="Optional OpenAI vector store ID for hosted FileSearchTool. May be repeated.",
    )
    parser.add_argument(
        "--file-search-results",
        type=int,
        default=8,
        help="Maximum hosted file-search results when --vector-store-id is used.",
    )
    parser.add_argument(
        "--max-turns",
        type=int,
        default=12,
        help="Maximum Agents SDK turns before stopping.",
    )
    parser.add_argument(
        "--api-backend",
        choices=("auto", "responses", "agents"),
        default=os.environ.get("XSHI_MATH_DEEP_MATH_API_BACKEND", "auto"),
        help=(
            "API backend. 'auto' uses direct Responses API when no hosted tools "
            "are requested, otherwise the Agents SDK."
        ),
    )
    parser.add_argument(
        "--no-background",
        action="store_true",
        help="Disable background mode for direct Responses API runs.",
    )
    parser.add_argument(
        "--max-poll-seconds",
        type=float,
        default=float(
            os.environ.get(
                "XSHI_MATH_DEEP_MATH_MAX_POLL_SECONDS",
                str(DEFAULT_MAX_POLL_SECONDS),
            )
        ),
        help="Maximum wall-clock time to poll a background Responses API run.",
    )
    parser.add_argument(
        "--poll-interval-seconds",
        type=float,
        default=float(
            os.environ.get(
                "XSHI_MATH_DEEP_MATH_POLL_INTERVAL_SECONDS",
                str(DEFAULT_POLL_INTERVAL_SECONDS),
            )
        ),
        help="Seconds between background Responses API polls.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=float(os.environ.get("OPENAI_TIMEOUT", "900")),
        help="OpenAI client timeout for uploads and model calls.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build and print the context manifest without calling the API.",
    )
    return parser.parse_args(argv)


def read_prompt(args: argparse.Namespace) -> str:
    if args.prompt is not None:
        prompt = args.prompt.strip()
    else:
        prompt = args.prompt_file.read_text(encoding="utf-8", errors="replace").strip()
    if not prompt:
        raise SystemExit("The prompt is empty.")
    return prompt


def resolve_path(path: Path, repo_root: Path) -> Path:
    candidate = path if path.is_absolute() else repo_root / path
    return candidate.expanduser().resolve()


def relative_path(path: Path, repo_root: Path) -> str:
    try:
        return path.relative_to(repo_root).as_posix()
    except ValueError:
        return path.as_posix()


def iter_context_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
        return
    if not path.is_dir():
        return
    for root, dirs, files in os.walk(path):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in sorted(files):
            yield Path(root) / name


def discover_context_paths(args: argparse.Namespace) -> list[Path]:
    repo_root = args.repo_root
    roots: list[Path] = []
    if not args.no_default_context:
        roots.extend(repo_root / item for item in DEFAULT_CONTEXT)
    roots.extend(resolve_path(path, repo_root) for path in args.context)
    for pattern in args.context_glob:
        roots.extend(sorted(repo_root.glob(pattern)))

    discovered: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        if not root.exists():
            continue
        for path in iter_context_files(root):
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                discovered.append(resolved)
    return discovered


def read_inline_section(path: Path, repo_root: Path, max_inline_bytes: int) -> tuple[str, str | None]:
    rel = relative_path(path, repo_root)
    size = path.stat().st_size
    text = path.read_text(encoding="utf-8", errors="replace")
    truncated = False
    if len(text.encode("utf-8", errors="replace")) > max_inline_bytes:
        encoded = text.encode("utf-8", errors="replace")[:max_inline_bytes]
        text = encoded.decode("utf-8", errors="replace")
        truncated = True
    header = f"## File: {rel}"
    note = "\n\n[Truncated by runner size limit.]\n" if truncated else ""
    section = f"{header}\n\n<file path=\"{rel}\">\n{text}{note}</file>\n"
    warning = f"{rel}: truncated to {max_inline_bytes} bytes" if truncated else None
    return section, warning


def build_context_package(args: argparse.Namespace) -> ContextPackage:
    repo_root = args.repo_root
    max_inline_bytes = args.max_inline_kb * 1024
    max_attachment_bytes = args.max_attachment_mb * 1024 * 1024
    inline_sections: list[str] = []
    inline_paths: list[Path] = []
    pdf_paths: list[Path] = []
    image_paths: list[Path] = []
    skipped: list[str] = []

    for path in discover_context_paths(args):
        rel = relative_path(path, repo_root)
        suffix = path.suffix.lower()
        try:
            size = path.stat().st_size
        except OSError as exc:
            skipped.append(f"{rel}: cannot stat file ({exc})")
            continue

        if suffix in TEXT_EXTENSIONS:
            try:
                section, warning = read_inline_section(path, repo_root, max_inline_bytes)
            except OSError as exc:
                skipped.append(f"{rel}: cannot read text ({exc})")
                continue
            inline_sections.append(section)
            inline_paths.append(path)
            if warning:
                skipped.append(warning)
        elif suffix == ".pdf":
            if size <= max_attachment_bytes:
                pdf_paths.append(path)
            else:
                skipped.append(f"{rel}: PDF exceeds {args.max_attachment_mb} MB")
        elif suffix in IMAGE_EXTENSIONS:
            if size <= max_attachment_bytes:
                image_paths.append(path)
            else:
                skipped.append(f"{rel}: image exceeds {args.max_attachment_mb} MB")
        else:
            skipped.append(f"{rel}: unsupported extension {suffix or '[none]'}")

    return ContextPackage(
        inline_sections=inline_sections,
        inline_paths=inline_paths,
        pdf_paths=pdf_paths,
        image_paths=image_paths,
        skipped=skipped,
    )


def load_report_contract() -> str:
    contract_path = Path(__file__).resolve().parents[1] / "references" / "report_contract.md"
    return contract_path.read_text(encoding="utf-8", errors="replace")


def manifest_lines(package: ContextPackage, repo_root: Path) -> list[str]:
    lines = ["# Context Manifest", ""]
    lines.append("## Inlined Text Files")
    if package.inline_paths:
        lines.extend(f"- {relative_path(path, repo_root)}" for path in package.inline_paths)
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Attached PDFs")
    if package.pdf_paths:
        lines.extend(f"- {relative_path(path, repo_root)}" for path in package.pdf_paths)
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Attached Images")
    if package.image_paths:
        lines.extend(f"- {relative_path(path, repo_root)}" for path in package.image_paths)
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Skipped or Truncated")
    if package.skipped:
        lines.extend(f"- {item}" for item in package.skipped)
    else:
        lines.append("- None")
    return lines


def build_user_text(prompt: str, package: ContextPackage, repo_root: Path) -> str:
    manifest = "\n".join(manifest_lines(package, repo_root))
    inline_context = "\n\n".join(package.inline_sections) or "No text files were inlined."
    return "\n\n".join(
        [
            "# User Request\n\n" + prompt,
            load_report_contract(),
            manifest,
            "# Inline Repository Context\n\n" + inline_context,
        ]
    )


def import_openai_client():
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency 'openai'. Install it in the active runner "
            "environment with:\n"
            "  python3 -m pip install openai"
        ) from exc
    return OpenAI


def create_openai_client(timeout: float):
    OpenAI = import_openai_client()
    return OpenAI(timeout=timeout)


def attachment_content_parts(package: ContextPackage, repo_root: Path, client) -> list[dict]:
    parts: list[dict] = []
    for pdf_path in package.pdf_paths:
        rel = relative_path(pdf_path, repo_root)
        print(f"Uploading PDF: {rel}", file=sys.stderr)
        with pdf_path.open("rb") as handle:
            uploaded = client.files.create(file=handle, purpose="user_data")
        parts.append({"type": "input_file", "file_id": uploaded.id})

    for image_path in package.image_paths:
        rel = relative_path(image_path, repo_root)
        print(f"Embedding image: {rel}", file=sys.stderr)
        mime_type = mimetypes.guess_type(image_path.as_posix())[0] or "image/png"
        encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
        parts.append(
            {
                "type": "input_image",
                "image_url": f"data:{mime_type};base64,{encoded}",
                "detail": "high",
            }
        )
    return parts


def read_field(value, name: str, default=None):
    if isinstance(value, dict):
        return value.get(name, default)
    return getattr(value, name, default)


def as_plain(value):
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json", exclude_none=True)
    if hasattr(value, "dict"):
        return value.dict()
    if isinstance(value, list):
        return [as_plain(item) for item in value]
    if isinstance(value, tuple):
        return [as_plain(item) for item in value]
    if isinstance(value, dict):
        return {key: as_plain(item) for key, item in value.items()}
    if hasattr(value, "__dict__"):
        return {
            key: as_plain(item)
            for key, item in vars(value).items()
            if not key.startswith("_")
        }
    return str(value)


def compact_json(value) -> str:
    plain = as_plain(value)
    if plain is None:
        return "None"
    return json.dumps(plain, ensure_ascii=True, sort_keys=True)


def response_status(response) -> str:
    status = read_field(response, "status", "")
    return str(status or "").lower()


def response_id(response) -> str:
    return str(read_field(response, "id", "[no response id]"))


def response_output_item_types(response) -> list[str]:
    output = read_field(response, "output", []) or []
    return [str(read_field(item, "type", "[unknown]")) for item in output]


def response_usage_summary(response) -> str:
    usage = as_plain(read_field(response, "usage", None))
    if not isinstance(usage, dict):
        return "usage=None"
    output_details = usage.get("output_tokens_details") or {}
    return (
        "usage="
        f"input_tokens={usage.get('input_tokens')}, "
        f"output_tokens={usage.get('output_tokens')}, "
        f"reasoning_tokens={output_details.get('reasoning_tokens')}, "
        f"total_tokens={usage.get('total_tokens')}"
    )


def response_diagnostics(source: str, response) -> str:
    lines = [
        f"{source} response diagnostics:",
        f"- id: {response_id(response)}",
        f"- model: {read_field(response, 'model', '[unknown]')}",
        f"- status: {read_field(response, 'status', '[unknown]')}",
        f"- output item types: {', '.join(response_output_item_types(response)) or 'none'}",
        f"- {response_usage_summary(response)}",
    ]
    incomplete_details = read_field(response, "incomplete_details", None)
    if incomplete_details:
        lines.append(f"- incomplete_details: {compact_json(incomplete_details)}")
    error = read_field(response, "error", None)
    if error:
        lines.append(f"- error: {compact_json(error)}")
    return "\n".join(lines)


def extract_response_text(response) -> str:
    output_text = read_field(response, "output_text", None)
    if isinstance(output_text, str) and output_text.strip():
        return output_text

    text_parts: list[str] = []
    for item in read_field(response, "output", []) or []:
        for content in read_field(item, "content", []) or []:
            if read_field(content, "type", None) == "output_text":
                text = read_field(content, "text", "")
                if text:
                    text_parts.append(str(text))
    return "\n".join(text_parts)


def validate_response_output(source: str, response) -> str:
    status = response_status(response)
    if status != SUCCESS_RESPONSE_STATUS:
        raise SystemExit(
            f"{source} did not complete successfully.\n"
            f"{response_diagnostics(source, response)}"
        )

    output = extract_response_text(response).strip()
    if not output:
        raise SystemExit(
            f"{source} completed but returned no visible output.\n"
            f"{response_diagnostics(source, response)}"
        )
    return output


def validate_agent_output(result) -> str:
    output = str(read_field(result, "final_output", "") or "").strip()
    if output:
        return output

    lines = [
        "Agents SDK completed but returned no visible final_output.",
        "Agents SDK diagnostics:",
    ]
    raw_responses = read_field(result, "raw_responses", None) or []
    new_items = read_field(result, "new_items", None)
    lines.append(f"- raw_responses: {len(raw_responses)}")
    if new_items is not None:
        lines.append(f"- new_items: {len(new_items)}")
    if raw_responses:
        lines.append(response_diagnostics("Last raw response", raw_responses[-1]))
    raise SystemExit("\n".join(lines))


def import_agents_sdk():
    try:
        from agents import Agent, FileSearchTool, ModelSettings, Runner, WebSearchTool
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency 'openai-agents'. Install it with:\n"
            "  python3 -m pip install openai-agents"
        ) from exc
    return Agent, FileSearchTool, ModelSettings, Runner, WebSearchTool


def needs_hosted_tools(args: argparse.Namespace) -> bool:
    return (not args.no_web_search) or bool(args.vector_store_id)


def select_api_backend(args: argparse.Namespace) -> str:
    if args.api_backend == "responses":
        if needs_hosted_tools(args):
            raise SystemExit(
                "--api-backend responses can only be used when hosted tools are "
                "disabled. Pass --no-web-search and omit --vector-store-id, or "
                "use --api-backend agents."
            )
        return "responses"
    if args.api_backend == "agents":
        return "agents"
    return "agents" if needs_hosted_tools(args) else "responses"


def build_tools(args: argparse.Namespace, FileSearchTool, WebSearchTool) -> list:
    tools = []
    if not args.no_web_search:
        tools.append(WebSearchTool())
    if args.vector_store_id:
        tools.append(
            FileSearchTool(
                vector_store_ids=args.vector_store_id,
                max_num_results=args.file_search_results,
            )
        )
    return tools


def build_input_items(
    args: argparse.Namespace,
    prompt: str,
    package: ContextPackage,
    client=None,
) -> list[dict]:
    content_parts = [
        {"type": "input_text", "text": build_user_text(prompt, package, args.repo_root)}
    ]
    if package.pdf_paths or package.image_paths:
        upload_client = client or create_openai_client(args.timeout_seconds)
        content_parts.extend(attachment_content_parts(package, args.repo_root, upload_client))
    return [{"role": "user", "content": content_parts}]


def wait_for_background_response(client, response, args: argparse.Namespace):
    started = time.monotonic()
    status = response_status(response)
    while status in PENDING_RESPONSE_STATUSES:
        elapsed = time.monotonic() - started
        if elapsed > args.max_poll_seconds:
            raise SystemExit(
                "Responses API background run did not finish before "
                f"--max-poll-seconds={args.max_poll_seconds}.\n"
                f"{response_diagnostics('Responses API', response)}"
            )
        print(
            f"Response {response_id(response)} status={status}; "
            f"polling again in {args.poll_interval_seconds:g}s",
            file=sys.stderr,
        )
        time.sleep(args.poll_interval_seconds)
        response = client.responses.retrieve(response_id(response))
        status = response_status(response)
    return response


def run_responses_api(args: argparse.Namespace, prompt: str, package: ContextPackage) -> str:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set.")

    client = create_openai_client(args.timeout_seconds)
    input_items = build_input_items(args, prompt, package, client)
    request_kwargs = {
        "model": args.model,
        "instructions": AGENT_INSTRUCTIONS,
        "input": input_items,
        "max_output_tokens": args.max_output_tokens,
        "text": {"verbosity": args.verbosity},
        "truncation": "auto",
        "background": not args.no_background,
    }
    if args.reasoning_effort != "none":
        request_kwargs["reasoning"] = {"effort": args.reasoning_effort}

    started = time.monotonic()
    print(
        "Starting direct Responses API run "
        f"(background={'no' if args.no_background else 'yes'}, "
        f"max_output_tokens={args.max_output_tokens})",
        file=sys.stderr,
    )
    response = client.responses.create(**request_kwargs)
    if not args.no_background:
        print(
            f"Response {response_id(response)} started with status={response_status(response)}",
            file=sys.stderr,
        )
        response = wait_for_background_response(client, response, args)

    elapsed = time.monotonic() - started
    print(f"Responses API run completed in {elapsed:.1f}s", file=sys.stderr)
    print(response_diagnostics("Responses API", response), file=sys.stderr)
    return validate_response_output("Responses API", response)


def run_agent(args: argparse.Namespace, prompt: str, package: ContextPackage) -> str:
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set.")

    Agent, FileSearchTool, ModelSettings, Runner, WebSearchTool = import_agents_sdk()
    input_items = build_input_items(args, prompt, package)

    settings_kwargs = {
        "verbosity": args.verbosity,
        "max_tokens": args.max_output_tokens,
        "truncation": "auto",
    }
    if args.reasoning_effort != "none":
        settings_kwargs["reasoning"] = {"effort": args.reasoning_effort}
    model_settings = ModelSettings(**settings_kwargs)
    agent = Agent(
        name="xshi-math Deep Math Consultant",
        instructions=AGENT_INSTRUCTIONS,
        model=args.model,
        model_settings=model_settings,
        tools=build_tools(args, FileSearchTool, WebSearchTool),
    )
    started = time.monotonic()
    result = Runner.run_sync(agent, input_items, max_turns=args.max_turns)
    elapsed = time.monotonic() - started
    print(f"Agent run completed in {elapsed:.1f}s", file=sys.stderr)
    return validate_agent_output(result)


def run_model(args: argparse.Namespace, prompt: str, package: ContextPackage) -> str:
    backend = select_api_backend(args)
    print(f"Using API backend: {backend}", file=sys.stderr)
    if backend == "responses":
        return run_responses_api(args, prompt, package)
    return run_agent(args, prompt, package)


def dry_run_summary(args: argparse.Namespace, package: ContextPackage, prompt: str) -> str:
    prompt_preview = textwrap.shorten(prompt.replace("\n", " "), width=180, placeholder="...")
    backend = select_api_backend(args)
    background = (
        "disabled" if args.no_background else "enabled"
    ) if backend == "responses" else "not applicable"
    lines = [
        "Dry run only; no OpenAI API call was made.",
        f"Model: {args.model}",
        f"Reasoning effort: {args.reasoning_effort}",
        f"Verbosity: {args.verbosity}",
        f"Max output tokens: {args.max_output_tokens}",
        f"API backend: {backend}",
        f"Responses background: {background}",
        f"Web search: {'disabled' if args.no_web_search else 'enabled'}",
        f"Vector stores: {', '.join(args.vector_store_id) if args.vector_store_id else 'none'}",
        f"Prompt preview: {prompt_preview}",
        "",
        *manifest_lines(package, args.repo_root),
    ]
    return "\n".join(lines)


def write_output(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    args.repo_root = args.repo_root.expanduser().resolve()
    prompt = read_prompt(args)
    package = build_context_package(args)

    if args.dry_run:
        output = dry_run_summary(args, package, prompt)
    else:
        output = run_model(args, prompt, package)

    if args.output:
        write_output(args.output, output)
        print(f"Wrote {args.output}", file=sys.stderr)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
