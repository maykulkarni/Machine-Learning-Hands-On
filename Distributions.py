import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *


def uniform_distribution(low, high, points):
    data = np.random.uniform(low, high, points)
    plt.hist(data, 50)
    plt.show()


def pdf_normal_distribution(data):
    plt.plot(data, norm.pdf(data))
    plt.show()


def pdf_exponential_distribution(data):
    plt.plot(data, expon.pdf(data))
    plt.show()


def pdf_uniform(data):
    plt.plot(data, uniform.pdf(data))
    plt.show()


def pmf_binomial(data):
    n, p = 10, 0.5
    plt.plot(data, binom.pmf(data, n, p))
    plt.show()


def pmf_poisson(data):
    mu = 500
    plt.plot(data, poisson.pmf(data, mu))
    plt.show()

pmf_poisson(np.arange(400, 600, 0.5))
# lis = np.random.exponential(100, 1000000)

