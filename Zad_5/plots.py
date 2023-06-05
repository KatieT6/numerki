import numpy as np
from matplotlib import pyplot as plt

from AbstractBaseFunction import AbstractBaseFunction
from hermitePolynomial import ApproximationPolynomial


def plot_approximation(
        func: AbstractBaseFunction,
        approx: ApproximationPolynomial,
        left,
        right):

    fig = plt.figure()
    ax = plt.axes()

    ax.grid(True, axis="both")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    xs = np.linspace(left, right)
    y_original = [func(x) for x in xs]
    y_approx = [approx(x) for x in xs]

    ax.plot(xs, y_original, 'b', linestyle='dashed', label='original function')
    ax.plot(xs, y_approx, 'r', label='approximation function')

    plt.legend()
    plt.show()
