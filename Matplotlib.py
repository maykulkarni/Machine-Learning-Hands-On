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


def pie_chart():
    data = [12, 14, 16, 54]
    lables = ['US', 'Russia', 'China', 'India']
    explode = [0.1, 0.1, 0.1, 0.1]
    plt.pie(data, labels=lables, explode=explode)
    plt.show()


def bar_chart():
    x = np.random.randint(0, 500, 100)
    y = np.random.randint(0, 500, 100)
    plt.scatter(x, y)
    plt.show()


def histogram():
    data = np.random.normal(500, 10, 100000)
    plt.hist(data, bins=100)
    plt.show()


def box_whisker_plot():
    normal = np.random.randint(0, 100, 100)
    low_outlier = np.random.randint(-200, -100, 10)
    high_outlier = np.random.randint(200, 300, 10)
    normal = np.concatenate((normal, low_outlier, high_outlier))
    plt.boxplot(normal)
    plt.show()


# histogram()
box_whisker_plot()
