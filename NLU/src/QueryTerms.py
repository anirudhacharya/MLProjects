'''
Created on Apr 21, 2014

@author: Anirudh
'''
'''
fhandle = open('out.txt','w')
fhandle.write("Hello World")
"Jane knocked on Susan's door but she did not get an answer",
"Jane gave Joan candy because she was not hungry",
             "Emma did not pass the ball to Janice although she was open",
             "Emma did not pass the ball to Janice although she saw that she was open",
             "Kirilov ceded the presidency to Shatov because he was more popular",
             "Kirilov ceded the presidency to Shatov because he was less popular",
             "Dan had to stop Bill from toying with the injured bird, he was very compassionate"
'''
import nltk
sentences = ["Sid explained his theory to Mark but he could not convince him"] 

fHandle = open('out1.txt','w')
for sent in sentences:
    query = []
    tags = nltk.pos_tag(nltk.word_tokenize(sent))
    #print tags
    for i,j in tags:
        print i,j
        if j in ['VB','VBD','VBG', 'VBN', 'VBZ', 'JJ','RB','NNS']:
            #print i,j
            fHandle.write(i+" ")
    #fHandle.write('\n')
fHandle1 = open('data.txt','r')
data = fHandle1.read()
sent = data.split('\n')
fHandle.write(i+" ")
