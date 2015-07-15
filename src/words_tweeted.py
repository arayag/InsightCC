import csv
import sys

inputFile = sys.argv[1]
outputFile = open('tweet_output/ft1.txt', 'w')

with open(inputFile, 'rb') as ASCIIfile:
    LinesOfTweets = csv.reader(ASCIIfile, delimiter = ' ')  # Read in the data as "words" delimited by white space
    data = []                                               # Read this way, the data is already parsed into words
    for row in LinesOfTweets:                               # The rows here consist of a list of words in each tweet
        data.append(row)	


wordPairs = {}   # A Dictionary: advantage in lookups is (amortized) to O(1) as opposed to O(n) for a list. 
                 # See:  http://stackoverflow.com/questions/513882/python-list-vs-dict-for-look-up-table
for row in data: # Index FREE notation
    for word in row:
        if word not in wordPairs:
            wordPairs[word] = 1   # First instance of (key) 'word' stored in dictionary 
        else:
            wordPairs[word] += 1  # Update the occurrences of word in dictionary


for key in sorted(wordPairs.keys()):
    printStr =  key + ', '+ '\t\t' + str(wordPairs[key]) + '\n' # Construct a string to write to outputFile
    outputFile.write(printStr)                                  # for (word, counts) pairs
#    equivalently: print (key, wordPairs[key])


outputFile.close()
