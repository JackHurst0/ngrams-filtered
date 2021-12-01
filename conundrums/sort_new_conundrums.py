import csv


def getdata():
	conundrumlist = []
	with open('all-conundrums-ascension-aug2020.csv', 'r') as data:
		rows = csv.reader(data, delimiter=',')
		for row in rows:
			conundrumlist.append(row[0])
	return conundrumlist


def find_new_conundrums(new_conundrums):
	old_conundrums = []
	with open('all-conundrums.csv', 'r') as theirdata:
		rows = csv.reader(theirdata, delimiter=',')
		for row in rows:
			old_conundrums.append(row[0])

	diff = []

	for conundrum in new_conundrums:
		if conundrum not in old_conundrums:
			diff.append(conundrum)

	with open('new-conundrums-aug-2020.csv', 'w') as output:
		diff.sort()
		for conundrum in diff:
			output.write('{0}\n'.format(conundrum))

def main():
	old_conundrums = getdata()
	find_new_conundrums(old_conundrums)



if __name__ == '__main__':
	main()