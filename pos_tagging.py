#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:11:35 2020

@author: ritwik
"""


#Task-1
import nltk
from nltk.corpus import names
nltk.download('names')
names.words()
def gender_features(word):
    return {'last_letter':word[-1]}

gender_features('Trump')



name = names.words()

d1 ={}

labeled_names = ([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])

import random
random.shuffle(labeled_names)

feature = [(gender_features(n),gender) for (n,gender) in labeled_names]

train_set,test_set = feature[:5500],feature[5500:]

clf = nltk.NaiveBayesClassifier.train(train_set)

clf.show_most_informative_features(10)

clf.classify(gender_features('Ritwik'))

nltk.classify.accuracy(clf,test_set)
    

#POS tagging

from nltk.tag import pos_tag

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download('averaged_perceptron_tagger')
st = sent_tokenize(text)
wt = word_tokenize(text)

l1 = pos_tag(wt)
