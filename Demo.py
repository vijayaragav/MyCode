from sklearn import tree
features = [[150, 1], [170, 1], [130, 0], [140, 0]]
label = [1, 1, 0, 0]
cls = tree.DecisionTreeClassifier()
cls = cls.fit(features, label)
print(cls.predict([[150, 0]]))


