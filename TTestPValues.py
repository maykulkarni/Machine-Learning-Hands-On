import numpy as np
from scipy import stats

A = np.random.normal(25, 5, 10000)
B = np.random.normal(26, 5, 10000)
# t statistic is a measure of the difference of the two sets expressed in the units of standard
# error. Put differently it's the size of difference relative to the variance in the data.
# High T value means there's a real difference between two data, you have 'significance'

# P value is the measure of probability of the observation lying at extreme t values. So low p-value
# also implies significance.

# If you're looking at 'statistically significant' result, you'll see high t value and low p value.
print stats.ttest_ind(A, B)
