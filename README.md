Code repository for Insight code challenge.

The challenge is to produce scalable code to extract: 1- the words tweeted and their frequency and 2- the mean number of unique words per tweet 
from a given input file with lines of tweets as entries. 

In addition to this READ ME file, this directory also contains a bash file: run.sh and three sub-directories: tweet_input, tweet_output and and src. 

tweet_input contains test.txt and tweet.txt as test files for the source code.
The Python source code is located in src as two stand alone modules: words_tweeted.py and median_unique.py.
Output from these two modules is written to tweet_output/ft1.txt and tweet_output/ft2.txt, respectively.

Given that this challenge emphasis is on scalability of the source code to treat large data sets, I have attempted to use appropriate data structures
which speed up searching and sorting processes.  Accordingly, the use of both Python sets and dictionaries has been adopted in each of the two source
modules under the scr sub-directory when deemed appropriate.

Thank you for reading.

Rafael Araya-Gochez 7/14/2015
# InsightCC
