import time
start = time.clock()
import numpy as np
end = time.clock()
print('import numpy:', int((end-start)*1000), 'msec')
start = time.clock()
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
end = time.clock()
print('import lda:', int((end-start)*1000), 'msec')

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
y = np.array([1, 1, 1, 2, 2, 2])
start = time.clock()
clf = LinearDiscriminantAnalysis()
clf.fit(X, y)
end = time.clock()
print('fit lda:', int((end-start)*1000), 'msec')
# LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None,
#               solver='svd', store_covariance=False, tol=0.0001)
print(clf.predict([[-0.8, -1], [2, 2], [0, 0.001]]))
# [1]
X = np.array([[1, 1], [2, 1], [3, 2], [-1, -1], [-2, -1], [-3, -2]])
y = np.array([12, 12, 12, 31, 31, 31])
start = time.clock()
clf = LinearDiscriminantAnalysis()
clf.fit(X, y)
end = time.clock()
print('fit lda:', int((end-start)*1000), 'msec')
# LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None,
#               solver='svd', store_covariance=False, tol=0.0001)
print(clf.predict([[-0.8, -1], [2, 2], [0, 0.001]]))
# [1]
