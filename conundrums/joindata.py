import os
import csv

# Take the filtered ngrams data and condense down
# into one list of the entries 9 letters long
def getfiles():
	print('Getting files')
	files = [f for f in os.listdir(os.path.join('..','output','real')) if os.path.isfile(os.path.join('..','output','real', f)) and not f.startswith('.')]
	print('Got files {0}\n{1} files total'.format(files, len(files)))
	return [os.path.join('..','output','real', f) for f in files] 

def writeoutput(files):
	with open('9s-alphabetical.csv', 'w') as output:
		files.sort()
		for file in files:
			with open(file) as data:
				print('Opened {0}'.format(file))
				rows = csv.reader(data, delimiter=',')
				for row in rows:
					if len(row[0]) == 9:
						output.write('{0},{1}\n'.format(row[0], row[1]))


def main():
	files = getfiles()
	writeoutput(files)


if __name__ == '__main__':
	main()