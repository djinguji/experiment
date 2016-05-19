import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])

clf = LinearDiscriminantAnalysis()
clf.fit(X, y)
# LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None,
#               solver='svd', store_covariance=False, tol=0.0001)
print(clf.predict([[-0.8, -1], [2, 2], [0, 0.001]]))
# [1]
