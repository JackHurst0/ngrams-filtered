import csv


def getdata():
	conundrumlist = []
	word8s = []
	word7s = []
	with open('alphagrams-ranked.csv', 'r') as data:
		rows = csv.reader(data, delimiter=',')
		for row in rows:
			alphagram = row[1]
			words = row[2].split('/')
			if len(alphagram) == 9 and len(words) == 1:
				conundrumlist.append(words[0])
			elif len(alphagram) == 8:
				word8s.extend(words)
			elif len(alphagram) == 7:
				word7s.extend(words)
	return [conundrumlist, word8s, word7s]

# For a 9 letter word work out if it is a plural or not
def isplural(word, word8s, word7s):
	if word.endswith("ES") and word[:-2] in word7s:
		# print('{0} is an ES plural'.format(word))
		return True
	elif word.endswith("S") and word[:-1] in word8s:
		# print('{0} is an S plural'.format(word))
		return True
	elif word.endswith("IES") and word[:-3] + "Y" in word7s:
		# print('{0} is an IES plural'.format(word))
		return True
	return False

def writeoutput(conundrums):
	with open('our-conundrums.csv', 'w') as output:
		conundrums.sort()
		for conundrum in conundrums:
			output.write('{0}\n'.format(conundrum))

def findunusedconundrums(ourconundrums):
	theirconundrums = []
	with open('all-conundrums.csv', 'r') as theirdata:
		rows = csv.reader(theirdata, delimiter=',')
		for row in rows:
			theirconundrums.append(row[0])

	unrankedconundrums = []

	for conundrum in ourconundrums:
		if conundrum not in theirconundrums:
			unrankedconundrums.append(conundrum)

	with open('unranked-conundrums.csv', 'w') as output:
		unrankedconundrums.sort()
		for conundrum in unrankedconundrums:
			output.write('{0}\n'.format(conundrum))


def main():
	data = getdata()
	words = data[0]
	word8s = data[1]
	word7s = data[2]
	conundrums = [word for word in words if not isplural(word, word8s, word7s)]
	writeoutput(conundrums)
	findunusedconundrums(conundrums)




if __name__ == '__main__':
	main()