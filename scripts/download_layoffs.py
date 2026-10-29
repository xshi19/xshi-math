"""Download the layoffs.fyi Kaggle mirror to an ignored local directory.

Install the Kaggle CLI separately and configure your own credentials as described
at https://github.com/Kaggle/kaggle-cli. This script never reads/prints credentials.
The current mirror may differ from the 2026-10-26 snapshot used by the page.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import zipfile

from xmath.incerto.datasets import cache_path, load_layoffs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', type=Path,
                        default=cache_path('layoffs/layoffs.csv'))
    parser.add_argument('--version', type=int, help='Kaggle dataset version; default is latest')
    args = parser.parse_args()
    if args.version is not None and args.version < 1:
        parser.error('--version must be positive')
    if not shutil.which('kaggle'):
        parser.error('Install the Kaggle CLI and configure your own credentials first.')
    destination = args.destination.expanduser().resolve()
    if destination.exists():
        parser.error(f'{destination} already exists; choose a new destination')
    # Keep the archive, and isolate each download so existing files survive.
    # Kaggle --unzip deletes its archive, so extract the selected CSV ourselves.
    import tempfile
    destination.parent.mkdir(parents=True, exist_ok=True)
    download_dir = Path(tempfile.mkdtemp(prefix='download-', dir=destination.parent))
    dataset = 'swaptr/layoffs-2022'
    if args.version is not None:
        dataset += f'/{args.version}'
    subprocess.run(['kaggle', 'datasets', 'download', dataset, '-p', str(download_dir)],
                   check=True)
    archives = list(download_dir.glob('*.zip'))
    if len(archives) != 1:
        raise RuntimeError(f'Expected one Kaggle ZIP archive; inspect {download_dir}')
    with zipfile.ZipFile(archives[0]) as archive:
        candidates = [name for name in archive.namelist() if name.lower().endswith('.csv')]
        if len(candidates) != 1:
            raise RuntimeError(f'Expected one CSV; inspect {archives[0]}')
        # A fixed destination avoids trusting archive paths.
        with archive.open(candidates[0]) as source, destination.open('xb') as target:
            shutil.copyfileobj(source, target)
    data = load_layoffs(destination)
    print(f'Saved {destination}: {data.input_rows} rows, {data.count.size} company-date events.')
    print(f'Archive retained in {download_dir}. No files were deleted.')


if __name__ == '__main__':
    main()
