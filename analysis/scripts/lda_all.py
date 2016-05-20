import time

start = time.clock()
import numpy as np
end = time.clock()
print('import numpy:', int((end-start)*1000), 'msec')
start = time.clock()
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
end = time.clock()
print('import lda:', int((end-start)*1000), 'msec')
import sys

def add_file(file1, X, y, c):
	infile = open(file1) 
	input = infile.readlines()
	infile.close()
	print('read:', file1 + ', length:', len(input))
	for line in input:
		data = line.rstrip().split('\t')
		if len(data) < 2:
			return
		ident = data[0].split('+')
		vals = []
		for value in data[1:]:
			vals.append(float(value))
		X.append(vals)
		y.append(c)
	
def build(file1, file2, c1, c2):
	X = []
	y = []
	add_file(file1, X, y, c1)
	add_file(file2, X, y, c2)
	X = np.array(X)
	y = np.array(y)
	start = time.clock()
	clf = LinearDiscriminantAnalysis()
	clf.fit(X, y)
	end = time.clock()
	print('fit lda:', int((end-start)*1000), 'msec')
	print()
	return clf

def test(clf, file, c):
	data = []
	expected = []
	add_file(file, data, expected, c)
	response = clf.predict(data)
	print(response)
	print(np.array(expected))
	print()

def main():
	if len(sys.argv) == 5:
		file1 = sys.argv[1]
		file2 = sys.argv[2]
		test1 = sys.argv[3]
		test2 = sys.argv[4]
	else:
		file1 = 's_a.txt'
		file2 = 'sa.txt' 
		test1 = 's_at.txt'
		test2 = 'sat.txt'
	clf = build(file1, file2, 'X', '-')
	test(clf, test1, 'X')
	test(clf, test2, '-')
	
if __name__ == '__main__':
	main()
