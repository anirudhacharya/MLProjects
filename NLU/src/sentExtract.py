'''
Created on May 9, 2014

@author: Anirudh
'''
import nltk
fHandle = open('data.txt','r')
data = fHandle.read()
sentences = data.split('\n')
for sent in sentences:
    sent = sent.strip()
    if len(sent)>10:
        print sent
        sent1 = sent.split(',')
        for j in sent1:
            print j.strip()
        sent2 = sent.split(';')
        for j in sent1:
            print j.strip()