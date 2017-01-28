import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm


def create_cluster_data(N, k):
    np.random.seed(10)
    points_per_cluster = float(N) / k
    points_x = []
    points_y = []
    for i in range(k):
        income_centroid = np.random.uniform(20000, 200000)
        age_centroid = np.random.uniform(20, 70)
        for j in range(int(points_per_cluster)):
            points_x.append([np.random.normal(income_centroid, 10000, 1), np.random.normal(age_centroid, 5, 1)])
            points_y.append(i)
    points_x = np.array(points_x)
    points_y = np.array(points_y)
    return points_x, points_y


(X, y) = create_cluster_data(100, 5)
plt.scatter(X[:, 0], X[:, 1], c=y.astype(np.float))
plt.show()
C = 1.0
svc = svm.SVC(kernel='linear', C=C).fit(X, y)
