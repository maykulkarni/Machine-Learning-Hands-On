from itertools import cycle

import pylab as pl
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()
numSamples, numFeatures = iris.data.shape
print numSamples, numFeatures
print iris.target_names
X = iris.data
pca = PCA(n_components=2, whiten=True).fit(X)
X_pca = pca.transform(X)

# prints the amount of variance we've managed to preserved
print sum(pca.explained_variance_ratio_)

# Plot the graph
colors = cycle('rgb')
target_ids = range(len(iris.target_names))
pl.figure()
for i, c, label in zip(target_ids, colors, iris.target_names):
    pl.scatter(X_pca[iris.target == i, 0], X_pca[iris.target == i, 1],
               c=c, label=label)
    pl.legend()
pl.show()
