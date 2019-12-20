# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 16:45:50 2019

@author: Ritwik Gupta
"""

#20/12/19

from nltk.corpus import brown
brown.categories()
print(brown.words(categories='hobbies')[0:5])

from nltk.corpus import inaugural
inaugural.fileids()
inaugural.words(fileids='1933-Roosevelt.txt')[0:10]

from nltk.corpus import webtext
d1={}
for i in webtext.fileids():
    d1[i] = webtext.words(fileids=i)[:20]

#Downloaded the MASC data
import nltk
with open('tweets1.txt','r') as f:
    text = f.read().strip()
    text1 = text.split()
    text2 = nltk.Text(text1)
    text2.concordance("good",1)
    
#Project Gutenberg
from urllib import request
url="http://www.gutenberg.org/files/2554/2554-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf-8')
from nltk.tokenize import word_tokenize
tokens = word_tokenize(raw)
samp_text = nltk.Text(raw)