from sklearn.datasets import load_iris
from sklearn import tree
from numpy import *
iris = load_iris()
test_idx = [0, 50, 100]
# Training data
train_data = delete(iris.data, test_idx, axis=0)
train_target = delete(iris.target, test_idx)
# Testing
test_data = iris.data[test_idx]
test_target = iris.target[test_idx]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))


