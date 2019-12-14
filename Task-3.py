import nltk
nltk.download('inaugural')
nltk.download('book')
nltk.download()
from nltk.corpus import brown
brown.categories()
print(brown.words(categories='adventure'))
"""
Find the 50 most used words for each president
"""
from nltk.corpus import inaugural
inaugural.fileids()
inaugural.words(fileids='1861-Lincoln.txt')[0:10]
inaugural.words(fileids='2009-Obama.txt')

from nltk.book import *

f = nltk.FreqDist(inaugural.words(fileids='2009-Obama.txt'))
f.most_common(100)
