# N-grams filtered
This repository contains a filtered set of "words" harvested from the google n-grams project:
http://storage.googleapis.com/books/ngrams/books/datasetsv2.html

The purpose of this filtered set is to allow developers to have a quick accessible way of answering the question "how common is this word?". In previous projects over the years I've used n-grams to do this, and found myself writing scripts to wrangle with the data set which is very large and contains a lot of redundant information.

The data is reduced from 25GB to 58MB (500 times smaller!)

## Results
There are 26 files in `output/real`, one foe each letter of the alphabet. The filenames are based on the same syntax n-grams supplies it's data in.

Each file is a CSV containing all words found in the corpus beginning with that letter, along with a score. Here's a snippet of the file for the letter z

```
ZOOLOGV,538
ZOOLOGY,827353
ZOOLOJI,177
ZOOLOLOGICAL,49
ZOOLOO,360
```
The score for each word is the total number of times that word was observed in the corpus from books since the year 1920. Data going further bck was available but I felt it was less relevant.

Note the following:
- It only includes word which are entirely alphabetical characters
- It only includes words of 12 characters or less
- Words are store in a canonical upercase format
- There is a lot of junk in the list. For example in the above snippet you see `ZOOLOGV` which we assume to be the result of the OCR reading some books where the letter `Y` has not been printed very clearly in the word `ZOOLOGY`.
- The results do not form a suitable dictionary of any sort due to the junk mentioned above. If you are doing development for something like a word game (e.g an anagram solver) where you require exhaustive list of "valid" words, then this will not be suitable. You will need to source your own dictionary (plenty of open source dictionaries are available).

## Applications
- I've used this in my own word game (available on the Google Play Store: https://play.google.com/store/apps/details?id=uk.co.jackhurst.wordladders) to help generate levels which always have words deemed sufficiently common as answers.
- In games like WordScapes (popular anagram game) where the devloper only ever tends to have common words as the solutions to levels, you could use the results here to split the possible anagrams of a word into those deemed common enough to be "main answers" and those common enough to be "bonus answers", i.e those which aren't required to progress from the level but which nonetheless are still counted as valid is the user enters them
- If making a dictionary app you could use the results to enable a way for users to see how commonly used a word is.
- If trying to gauge the accessibility of written passages of texts, you could use the results as building blocks for scoring the accessibility of the passage.

## The scripts
There are 2 scripts used to harvest and filter the data. If you wish to modify the results you will want to look at editing the filter script:
`scripts/download.py`
`scripts/filter.py`

I've not written any python in about 5 years, so the code is probably not the nicest to read. Sorry! Reviews and PRs always welcome.

### Usage
- Run `download.py` to download ad unzip all of the data. You'll need at least 25GB storage free on your machine, and this will download over 10GB of data. The script  will take a while to run, varying according to your download speed. It took about 10 minutes for me on an fast fibre connection.
- After you have all the raw data use `filter.py` to filter it and generate output.
- 
### Dependencies
- python
- python requests library