import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale


def create_cluster_data(N, k):
    np.random.seed(10)
    points_per_cluster = float(N) / k
    points_x = []
    points_y = []
    for i in range(k):
        income_centroid = np.random.uniform(20000, 200000)
        age_centroid = np.random.uniform(20, 70)
        for j in range(int(points_per_cluster)):
            points_x.append(np.random.normal(income_centroid, 10000, 1))
            points_y.append(np.random.normal(age_centroid, 5, 1))
    points_x = np.array(points_x)
    points_y = np.array(points_y)
    return points_x, points_y


def k_means():
    x, y = create_cluster_data(100, 5)
    plt.scatter(x, y)
    plt.show()
    clf = KMeans(n_clusters=5)
    clf = clf.fit(scale(x), scale(y))
    print clf.labels_
    plt.scatter(x, y, c=clf.labels_.astype(np.float))
    plt.show()


if __name__ == '__main__':
    k_means()
