import matplotlib.pyplot as plt
import numpy as np

from StatsBasics import *


def de_mean(data):
    mean_x = mean(data)
    return [x - mean_x for x in data]


def sample_covar(data_1, data_2):
    x_1 = np.array(de_mean(data_1))
    x_2 = np.array(de_mean(data_2))
    return x_1.dot(x_2) / (len(data_1) - 1)


def correlation(x, y):
    stddevx = x.std()
    stddevy = y.std()
    return sample_covar(x, y) / stddevx / stddevy


if __name__ == '__main__':
    pageSpeeds = np.random.normal(3, 1, 1000)
    purchaseAmount = np.random.normal(50, 10, 1000) * pageSpeeds
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.show()
    print sample_covar(pageSpeeds, purchaseAmount)
    print np.cov(pageSpeeds, purchaseAmount)
    print correlation(pageSpeeds, purchaseAmount)
