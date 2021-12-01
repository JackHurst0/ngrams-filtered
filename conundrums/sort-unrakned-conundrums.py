import os
import csv

# Sort existing data to get most frequent values at the top

def getdata():
	conundrumlist = []
	with open('unranked-conundrums.csv', 'r') as data:
		rows = csv.reader(data, delimiter=',')
		for row in rows:
			conundrumlist.append(row[0])
	return conundrumlist


def writedata(words):
	with open('9s-commonality.csv', 'r') as data:
		rows = csv.reader(data, delimiter=',')
		with open ('unranked-conundrums-commonality.csv', 'w') as ouput:
			for row in rows:
				if row[0] in words:
					ouput.write('{0},{1}\n'.format(row[0], row[1]))
				


def main():
	conundrums = getdata()
	writedata(conundrums)


if __name__ == '__main__':
	main()