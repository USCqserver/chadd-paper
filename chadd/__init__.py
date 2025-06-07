import numpy as np
from scipy.stats import bootstrap


def generate_bootstrap_distribution(
    data: np.array,
    statistic: callable = np.mean,
    num_bootstrap_resamples: int = 1000,
    confidence_level: float = 0.95,
) -> np.ndarray:
    rng = np.random.default_rng()
    data = (data,)
    res = bootstrap(
        data=data,
        statistic=statistic,
        n_resamples=num_bootstrap_resamples,
        confidence_level=confidence_level,
        method='percentile',
        random_state=rng,
    )
    return res.bootstrap_distribution
