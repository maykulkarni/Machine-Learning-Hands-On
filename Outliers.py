import matplotlib.pyplot as plt
import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
incomes = np.append(incomes, [1e9])


# plt.hist(incomes, 50)
# plt.show()  # bad! single outlier ends up skewing the entire data!
# print incomes.mean()


def filter(data):
    """
    Remove data from 2 standard deviations away
    :param data: list
    :return: filtered data
    """
    u = np.mean(data)
    s = np.std(data)
    filtered = [e for e in data if u - 2 * s <= e <= u + 2 * s]
    return filtered


incomes = filter(incomes)
plt.hist(incomes, 50)
plt.show()
print np.mean(incomes)
