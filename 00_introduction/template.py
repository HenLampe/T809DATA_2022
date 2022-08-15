from math import pi
import numpy as np
import matplotlib.pyplot as plt


def normal(x: np.ndarray, sigma: float, mu: float) -> np.ndarray:
    a = 1/np.power(2*pi*np.power(sigma, 2), 0.5)
    b = np.power((x-sigma), 2)
    c = 2 * np.power(mu, 2)
    return a * np.exp(-(b / c))
 
#def plot_normal(sigma: float, mu:float, x_start: float, x_end: float):
    # Part 1.2

#def _plot_three_normals():
    # Part 1.2

#def normal_mixture(x: np.ndarray, sigmas: list, mus: list, weights: list):
    # Part 2.1

#def _compare_components_and_mixture():
    # Part 2.2

#def sample_gaussian_mixture(sigmas: list, mus: list, weights: list, n_samples: int = 500):
    # Part 3.1

#def _plot_mixture_and_samples():
    # Part 3.2

if __name__ == '__main__':
    print(normal(3, 1, 5))
    # select your function to test here and do `python3 template.py`