import csv
import sys

inputFile = sys.argv[1]
outputFile = open('tweet_output/ft2.txt', 'w')

with open(inputFile, 'rb') as ASCIIfile:
    LinesOfTweets = csv.reader(ASCIIfile, delimiter = ' ')   # Read in the data as "words" delimited by white space.
    data = []
    for row in LinesOfTweets:
        data.append(row)	

numOfTweets = 0
med_Unique = 0.0
printStr = ''

for row in data:            # Index FREE notation
    numOfTweets += 1
    uniqueWords = set()     # SET here has advantage over list as it has O(1) lookups and smaller than dictionary. 
    numUniqWords = 0        # Allegedly dictionary is slightly faster than sets for large data sets but 
    for word in row:        # the number of items here is very small (words in each tweet) so a SETS is appropriate.
        if word not in uniqueWords:
            uniqueWords.update([word])     # Note the [] inside update to keep the word "together" within the set
            numUniqWords += 1           
    med_Unique = ( med_Unique * (numOfTweets-1) + numUniqWords ) / numOfTweets  # Easy formula, no delays!
#    printStr =  str(numUniqWords) + ', '+ str(med_Unique) + '\n' 
    printStr = str(med_Unique) + '\n' 
    outputFile.write(printStr)    

outputFile.close()