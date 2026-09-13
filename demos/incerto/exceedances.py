"""Run with: uv run python demos/incerto/exceedances.py."""

import numpy as np

from xmath import exceedance_fraction


def main() -> None:
    # Fixed synthetic observations; no data download or random seed is needed.
    observations = np.array([1.0, 2.0, 2.0, 4.0])
    for threshold in (0.0, 2.0, 4.0):
        fraction = exceedance_fraction(observations, threshold)
        print(f"threshold={threshold:g}: fraction strictly above={fraction:.2f}")


if __name__ == "__main__":
    main()
