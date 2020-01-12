# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 11:56:20 2020

@author: Ritwik Gupta
"""
#This corpus consists of 5 different departments from the Patrika newspaper in Hindi. The departments are Automobile,Sports,health,gadget and entertainment.

import os
#IndianCorpusReader is a package which helps read and tokenize majority of the Indian Languages
from nltk.corpus import IndianCorpusReader
corpusdir = 'Patrika/news'
#Redirect to the corpus destination
corpus = os.listdir(corpusdir)

#Create the corpus with 5 text files in Hindi
newcorpus = IndianCorpusReader("./Patrika/news",corpus)

#Read the files in the corpus
for i in sorted(newcorpus.fileids()):
    print(i)
    with newcorpus.open(i) as f:
        print(f.read().strip())
#print(newcorpus.words("automobile_final_text.txt"))
        
#print(newcorpus.raw().strip())

#Print the 5 files ids present in the corpus
print(newcorpus.fileids())

#Check the content of the health file
newcorpus.words(fileids='health_final_text.txt')[0:10]

#Sentence and word tokenize the health file from the corpus
from nltk.tokenize import word_tokenize,sent_tokenize
health = word_tokenize("".join(newcorpus.words(fileids='health_final_text.txt')))
health_sentences = sent_tokenizer("".join(newcorpus.sent_tokenizer(fileids = "health_final_text.txt")))
