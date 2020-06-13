import requests
import os
import gzip
import shutil


fileprefix = 'http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-1gram-20120701'
remoteFiles = ['{0}-{1}.gz'.format(fileprefix, letter) for letter in 'abcdefghijklmnopqrstuvwxyz']


def downloadFile(fileUrl):
	print('Downloading {0}'.format(fileUrl))

	filename = os.path.join('..', 'res', 'real',fileUrl.split("/")[-1])

	r = requests.get(fileUrl)

	print('Writing to gz file: {0}'.format(filename))

	with open(filename, 'w') as file:
		file.write(r.content)
	unzipFile(filename)


def unzipFile(filename):
	newfile = filename.replace(".gz", "")
	print 'Unzipping {0}'.format(filename)
	with gzip.open(filename, 'rb') as input:
		with open(newfile, 'wb') as output:
			shutil.copyfileobj(input, output)
	print 'Unzipped {0}'.format(filename)
	os.remove(filename)
	print 'Deleted {0}'.format(filename)

def main():
	for file in remoteFiles:
		downloadFile(file)

if __name__ == '__main__':
	main()
