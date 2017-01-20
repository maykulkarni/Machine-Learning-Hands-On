import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2)
pageSpeed = np.random.normal(3, 1, 1000)
purchaseAmount = np.random.normal(50, 10, 1000) / pageSpeed
plt.scatter(pageSpeed, purchaseAmount)
x = np.array(pageSpeed)
y = np.array(purchaseAmount)
xp = np.linspace(0, 7, 100)
predicts = np.poly1d(np.polyfit(x, y, 5))
plt.plot(xp, predicts(xp), c='r')
plt.show()
