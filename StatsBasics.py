import numpy as np
from scipy import stats as sp
import matplotlib.pyplot as plt


def plot_hist(data):
    plt.hist(data)
    plt.show()


def mean_median_mode(data):
    print 'mean : %r' % np.mean(data)
    print 'median : %r' % np.median(data)
    print sp.mode(data)


def std_var(np_array):
    print 'Std dev : %r' % np_array.std()
    print 'var : %r' % np_array.var()


def xth_percentile(data, x):
    np_a = np.array(data)
    print np.percentile(np_a, x)


def moments(data):
    np_array = np.array(data)
    print 'First moment: Mean = %r' % np_array.mean()
    print 'Second moment: Variance = %r' % np_array.var()
    print 'Third moment: Skewness = %r' % sp.skew(np_array)
    print 'Fourth moment: Kurtosis = %r' % sp.kurtosis(np_array)

xth_percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 99)
