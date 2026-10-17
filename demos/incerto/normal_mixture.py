"""Two multivariate normals using public SciPy APIs, without private subclasses.

Replaces the useful construction in legacy/src/multivariate_distributions.py
from incerto-wiki at 9717c9cf83aee18b47f423a14bce2f0d14bb8bcb.
Copyright (c) 2023 xshi19; MIT (see THIRD_PARTY_NOTICES.md).
This educational example is independent of the upstream Normix package.
"""
import numpy as np
from scipy.stats import multivariate_normal


def main():
    rng = np.random.default_rng(20261017)
    means = np.array([[0.0, 0.0], [1.0, -1.0]])
    covariances = np.array([np.eye(2), [[2.0, 0.5], [0.5, 1.0]]])
    weight = 0.3
    n = 100_000
    first = rng.random(n) < weight
    sample = np.empty((n, 2))
    sample[first] = rng.multivariate_normal(means[0], covariances[0], size=first.sum())
    sample[~first] = rng.multivariate_normal(means[1], covariances[1], size=(~first).sum())
    delta = means[0] - means[1]
    mean = weight * means[0] + (1 - weight) * means[1]
    covariance = (weight * covariances[0] + (1 - weight) * covariances[1]
                  + weight * (1 - weight) * np.outer(delta, delta))
    density_at_zero = sum(w * multivariate_normal(m, c).pdf([0, 0])
                          for w, m, c in zip([weight, 1 - weight], means, covariances))
    print("Mean (theory/sample):", mean, sample.mean(axis=0))
    print("Covariance (theory/sample):", covariance, np.cov(sample, rowvar=False))
    print("Density at origin:", density_at_zero)


if __name__ == "__main__":
    main()
