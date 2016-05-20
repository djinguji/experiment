# separate file

import sys

def main():
	filename = sys.argv[1]
	infile = open(filename + '.txt')
	lines = infile.readlines()
	infile.close()
	out1 = open(filename + '1.txt', 'w')
	out2 = open(filename + '2.txt', 'w')
	
	spkr = 'x'
	word = 'x'
	for line in lines:
		data = line.split('+')
		if data[0] == spkr and data[1] == word:
			out2.write(line)
		else:
			out1.write(line)
			spkr = data[0]
			word = data[1]
		
	out1.close()
	out2.close()

if __name__ == '__main__':
	main()