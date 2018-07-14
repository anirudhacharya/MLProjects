'''
Created on May 8, 2014

@author: Anirudh
'''
import nltk

f1 = open('text1.txt','r')
f2 = open('text2.txt','r')
line1 = f1.readline()
line2 = f2.readline()
fHandle = open('out.txt','a')
fHandle.truncate()

while line1 != None or line1!="":
    tags = nltk.pos_tag(nltk.word_tokenize(line1))
    query = ""
    for i,j in tags:
        if j in ['VB','VBD','VBG', 'JJ','RB','NNS']:
            query = query +i+" "
    fHandle.write(line1)
    fHandle.write(query+'\n'+'\n')
    query = ""
    tags = nltk.pos_tag(nltk.word_tokenize(line2))
    for i,j in tags:
        if j in ['VB','VBD','VBG', 'JJ','RB']:
            query = query +i+" "
    fHandle.write(line2)
    fHandle.write(query+'\n'+'\n')
    line1 = f1.readline()
    line2 = f2.readline()
    if line1=="":
        break