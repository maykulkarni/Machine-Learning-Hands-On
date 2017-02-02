from math import sqrt

import matplotlib.pyplot as plt
import numpy as np
from pyspark import SparkConf, SparkContext
from pyspark.mllib.clustering import KMeans
from sklearn.preprocessing import scale

conf = SparkConf().setMaster('local').setAppName('KMeansSpark')
sc = SparkContext(conf=conf)


def create_fake_clustered_data(N, k):
    """
    Create fake clustered data, clustered for N points
    in k clusters
    :param N: number of points
    :param k: number of clusters
    :return: fake clustered data in numpy array
    """
    np.random.seed(10)
    points_per_cluster = float(N) / k
    X = []
    for i in range(k):
        income_centroid = np.random.uniform(20000, 200000)
        age_centroid = np.random.uniform(20, 70)
        for j in range(int(points_per_cluster)):
            X.append([np.random.normal(income_centroid, 15000), np.random.normal(age_centroid, 3.5)])
    X = np.array(X)
    return X


def visualize(X):
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()


def error(point):
    """
    Computes WSSSE (Within Set Sum of Squared Errors)
    :param clusters: KMeans cluster object
    :param point:
    :return: WSSSE
    """
    centre = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x ** 2 for x in (point - centre)]))


if __name__ == '__main__':
    number_of_points = 100
    k = 5
    data = sc.parallelize(scale(create_fake_clustered_data(number_of_points, k)))

    # build cluster
    clusters = KMeans.train(data, k, maxIterations=10, runs=10, initializationMode='random')

    result_RDD = data.map(lambda points: clusters.predict(points)).cache()
    # Every time you hit an action, Spark computes a DAG to find the optimal execution
    # so while running two operations, it's recommended to cache the action so that
    # DAG won't run again
    # It's important to cache whenever you're doing more than one actions at a time
    print 'Counts by value: '
    counts = result_RDD.countByValue()
    print counts

    print 'Cluster assignment: '
    results = result_RDD.collect()
    print results

    WSSSE = data.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print 'WSSSE: '
    print WSSSE
    # error(data[0], clusters)
