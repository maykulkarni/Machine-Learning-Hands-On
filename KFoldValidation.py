from sklearn import datasets
from sklearn import model_selection
from sklearn import svm

iris = datasets.load_iris()
# reserve 40 % for testing and 60% for training
X_train, X_test, y_train, y_test = model_selection.train_test_split(iris.data, iris.target, test_size=0.4,
                                                                    random_state=0)
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print clf.score(X_test, y_test)

scores = model_selection.cross_val_score(clf, iris.data, iris.target, cv=5)
print scores
print scores.mean()

# For polynomial kernel, there are couple of runs with perfect accuracy 100% and couple with lower
# 90% accuracy which proves polynomial kernel is probably overfitting, so training_test would'nt come up with this
print '*' * 30
clf2 = svm.SVC(kernel='poly', C=1, degree=6).fit(X_train, y_train)
print clf.score(X_test, y_test)
scores = model_selection.cross_val_score(clf, iris.data, iris.target, cv=5)
print scores
print scores.mean()
