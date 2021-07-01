from sklearn import tree

# features = [[140, 1], [130, 1], [150, 0], [170, 0]]
# labels = [0, 0, 1, 1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print(clf.predict([[150, 0]]))

# features = [[150, 9], [200, 8], [300, 2], [450, 2]]
# labels = ["Minivan", "Minivan", "Sports-Car", "Sports-Car"]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)  # Fit means to TRAIN, we assume that it's training
# print(clf.predict([[150, 9]]))

features = [[2, 100], [6, 25], [1, 300], [1, 1000], [4, 100], [10, 100]]
labels = [1, 2, 1, 1, 2, 2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[6, 100]]))
