import os
import csv

# Sort existing data to get most frequent values at the top

def getdata():
	with open('9s-alphabetical.csv', 'r') as input:
		rows = csv.reader(input, delimiter=',')
		output = [{'word': row[0], 'score': row[1]} for row in rows]
	output.sort(key=lambda x: int(x['score']), reverse=True)
	return output


def writedata(words):
	with open('9s-commonality.csv', 'w') as output:
		for word in words:
			output.write('{0},{1}\n'.format(word['word'], word['score']))


def main():
	words = getdata()
	writedata(words)


if __name__ == '__main__':
	main()