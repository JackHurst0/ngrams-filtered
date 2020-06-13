import csv
import os
import itertools
import sys

# Group frequency of words together based on number of appearances in
# last 100 years.
# Remove any words which aren't alphabetical characters only or are
# longer than 12 characters

def filterData(filename):
	testMode = False
	if testMode:
		filePath = os.path.join('..', 'res', 'test', 'test-data.csv')
		output = os.path.join('..', 'output', 'test','a-test.csv')
		progressInterval = 10
	else:
		filePath = os.path.join('..','res','real', filename)
		output = os.path.join('..', 'output', 'real', 'filtered-{0}.csv'.format(filename))
		progressInterval = 1000000

	wordScores = {}
	with open(filePath) as data:
		rows = csv.reader(data, delimiter='\t')
		idx = 0
		for row in rows:
			idx+= 1
			if idx%progressInterval == 0:
				print '{0} lines  of {1} read'.format(idx, filename)
			word = row[0].upper()
			year = row[1]
			if word.isalpha() & (int(year) > 1920) & (len(word) <= 12):
				score = row[2]
				oldScore = wordScores.get(word, 0)
				wordScores[word] = oldScore + int(score)

	keys = wordScores.keys()
	keys.sort()

	print 'Writing data to {0}'.format(output)
	with open(output, "w") as file:
		for key in keys:
			file.write("{0},{1}\n".format(key, wordScores[key]))

def main():
	inputfiles = [f for f in os.listdir(os.path.join('..','res','real')) if os.path.isfile(os.path.join('..','res','real', f)) and not f.startswith('.')]
	print 'Input files are {}'.format(inputfiles)
	for file in inputfiles:
		filterData(file)

if __name__ == '__main__':
	main()
