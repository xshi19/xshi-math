"""Run local S&P loss diagnostics without fetching or exporting data.

Adapted from incerto-wiki at 9717c9cf83aee18b47f423a14bce2f0d14bb8bcb.
Copyright (c) 2023 xshi19; MIT (see THIRD_PARTY_NOTICES.md).
"""
import numpy as np
from xmath.incerto.datasets import DatasetNotAvailable, load_sp500_prices
from xmath.incerto.estimators import hill_alpha_estimator, mean_excess


def main():
    try:
        prices = load_sp500_prices(fetch=False)
    except DatasetNotAvailable:
        print("No local S&P cache. Financial data to be provided later via the Portfolio Manager bot.")
        return
    _, losses = prices.negative_log_returns()
    print(f"Window: {prices.date[0]} to {prices.date[-1]}; {len(losses)} loss days")
    for k in (25, 50, 100, 200, 400):
        if k < len(losses):
            print(f"k={k}: Hill alpha={hill_alpha_estimator(losses, k):.3f}")
    if len(losses) >= 20:
        print(mean_excess(losses, np.quantile(losses, [0.8, 0.9, 0.95]), min_exceedances=5))


if __name__ == "__main__":
    main()
