import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score

np.random.seed(2)
pageSpeeds = np.random.normal(3, 1, 100)
purchaseAmount = np.random.normal(50, 30, 100) / pageSpeeds

trainX = pageSpeeds[:80]
testX = pageSpeeds[80:]

trainY = purchaseAmount[:80]
testY = purchaseAmount[80:]

x = np.array(trainX)
y = np.array(trainY)

xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.axes().set_xlim([0, 7])
plt.axes().set_ylim([0, 200])
for degree in range(1, 10):
    p8 = np.poly1d(np.polyfit(x, y, degree))
    plt.plot(xp, p8(xp))
    print degree, r2_score(testY, p8(testX))
# plt.plot(xp, np.poly1d(np.polyfit(x, y, 2))(xp))
plt.show()
# print r2_score(testY, p8(testX))
