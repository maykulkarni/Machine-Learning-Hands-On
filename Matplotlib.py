import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp


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


def adjust_axes():
    plt.xkcd()
    axes = plt.axes()
    axes.set_xlim([-5, 5])
    axes.set_ylim([0, 1.0])
    axes.grid()  # Adds grid
    multiple_line_plot()
    print 'done'


# multiple_line_plot()
# line_plot()
adjust_axes()
