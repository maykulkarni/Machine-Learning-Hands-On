import scipy.stats as sp
import matplotlib.pyplot as plt
import numpy as np


def line_plot():
    lis = np.arange(-3, 3, 0.001)
    plt.plot(lis, sp.norm.pdf(lis))
    plt.show()


def multiple_line_plot():
    lis = np.arange(-3, 3, 0.001)
    # lis2 = np.arange(-2, 4, 0.001)
    plt.plot(lis, sp.norm.pdf(lis))
    plt.plot(lis, sp.norm.pdf(lis, 1, 1.5))
    plt.show()

multiple_line_plot()