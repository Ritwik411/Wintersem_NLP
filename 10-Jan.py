
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:02:43 2020

@author: Ritwik Gupta
"""


"""
Types of Lexicons
1.Mere Wordlis -- stopwords
2. Word list with info(Pronounciation) --cmu wordlist
3. Word list with Semantic Orientation --wordnet

Task 1 
1.Lexical Source
1.1 Stop Words in English + 1 More Language

"""
#Lixcon 1
from nltk.corpus import stopwords
word_list = stopwords.words('English')
words_spanish = stopwords.words('Spanish')
words_french = stopwords.words('french')

#CMU wordlist - Lexicon 2
import nltk 
entries = nltk.corpus.cmudict.entries()
len(entries)
#for i in entries[100000:100025]:
 #   print(i)
print(entries[1000:1050])

#lexicon 3 - Wordnet
from nltk.corpus import wordnet as w
w.synsets('motorcar')
w.synset('car.n.01').lemma_names() #head lemmas

w.synsets('ecstatic')
w.synset('ecstatic.s.01').lemma_names() #head lemmas

#Favourite Actor - Rami Malek

texts = ["""Rami Said Malek (English: /ˈrɑːmi ˈmælɪk/;[1][2] Arabic: رامي سعيد مالك‎, Egyptian Arabic: [ˈɾɑːmi sæˈʕiːd ˈmæːlek]; born May 12, 1981) is an American actor and producer. His breakthrough role was as computer hacker Elliot Alderson in the USA Network television series Mr. Robot (2015–2019), for which he received several accolades, including the 2016 Primetime Emmy Award for Outstanding Lead Actor in a Drama Series. In 2018, he portrayed rock singer and songwriter Freddie Mercury in the biopic Bohemian Rhapsody, for which he received critical acclaim and won several awards, including the Academy Award, Golden Globe Award, Screen Actors Guild Award, and British Academy Film Award for Best Actor. 
He is the first actor of Egyptian heritage to win the Academy Award for Best Actor.
[3] Time magazine named Malek one of the 100 most influential people in the world in 2019.
Born and raised in Los Angeles, California, to Egyptian immigrant parents, Malek studied theater at the University of Evansville in Indiana. He began his acting career performing plays in New York City theaters before returning to Los Angeles, where he found supporting roles in film and television, including the Fox sitcom The War at Home (2005–2007), the HBO miniseries The Pacific (2010), and the Night at the Museum film trilogy (2006–2014). He has done voicework for television and video games, as well as motion capture for the latter."""] 
#NLTK pipiline
for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        tagged_words = nltk.pos_tag(words)
        print(tagged_words)
    

#Working with Twitter
from nltk.tokenize import TweetTokenizer
text = 'The party was sooo fun :D #superfun'
twttkn = TweetTokenizer()
twttkn.tokenize(text)

#AndrewYNG
text = "The new UN Climate report shows our planet is nearing crisis.While individuals tweaking their carbon footprint is a good step, we now need more than that."
twttkn = TweetTokenizer()
twttkn.tokenize(text)

#Just splits the charcets based on space, may have loopholes 

