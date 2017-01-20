import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

pageSpeeds = np.random.normal(3, 1, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 1 / 5
# purchaseAmount = np.random.normal(19, 1, 1000)
plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()
slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)
print r_value ** 2


def predict(x):
    return slope * x + intercept


fitline = predict(pageSpeeds)
plt.plot(pageSpeeds, fitline, c='r')
plt.show()
