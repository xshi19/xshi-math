---
name: xshi-math-git-conventions
description: Handle xshi-math git operations deliberately. Use when staging, committing, branching, pushing, preparing pull requests, checking worktree status, preserving user changes, writing commit messages, or deciding what belongs in a commit.
---

# xshi-math Git Conventions

Use this skill when staging, committing, branching, pushing, or preparing a
pull request.

## Intent

Make git operations explicit, reviewable, and easy to recover from. Preserve
the user's worktree. Do not rewrite history or discard changes unless the user
explicitly asks.

## Workflow

1. Inspect current state:
   - `git status --short`
   - `git rev-parse --abbrev-ref HEAD`
   - `git remote -v`
2. Identify the intended commit scope.
3. If unrelated existing changes are present, keep them out of the commit unless
   the user asks to include them.
4. Run the smallest useful verification before committing (docs: link/read
   checks; Python: `uv run pytest` when code changes; site: `npm run build` /
   `npm run check:html` when HTML is in scope).
5. Stage deliberately with pathspecs; use `git add -A` only when the full
   worktree is the intended scope.
6. Review staged changes with `git diff --cached --stat`.
7. Commit with a concise imperative message. Prefer conventional-commit style
   when it helps review:
   - `docs(skills): add xshi-math concept-page skill`
   - `docs(rules): add shared-notation rule body`
   - `fix(demo): reject empty exceedance sample`
   Scopes that fit this repo: `skills`, `rules`, `design`, `plan`, `incerto`,
   `ig`, `normix-theory`, `site`, `demo`, `arch`.
8. Push the current branch to its upstream (`git push -u origin <branch>` when
   none exists). Open a PR with `gh pr create` when requested.

## Safety Rules

- Never run `git reset --hard`, destructive checkout, or force-push unless the
  user explicitly requests it.
- Do not amend an existing commit unless the user asks and the amend is safe.
- Do not stash user changes as a reflex.
- Do not change git `user.name` / `user.email` config; set `GIT_AUTHOR_*` /
  `GIT_COMMITTER_*` for a single commit when needed.
- Before pushing, confirm the branch name and remote.
- If verification cannot run, mention that in the final response.

## Completion Check

Before reporting done:

- `git status --short` has no unexpected staged changes left behind;
- the commit hash is known if a commit was created;
- the push target and PR URL are known if performed;
- verification results and any skipped checks are reported.
