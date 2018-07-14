'''
Created on Apr 21, 2014

@author: Anirudh
'''

import nltk
sentences = ["Jane gave Joan candy because she was hungry", 
             "Jane gave Joan candy because she was not hungry",
             "Emma did not pass the ball to Janice although she was open",
             "Emma did not pass the ball to Janice although she saw that she was open",
             "Kirilov ceded the presidency to Shatov because he was more popular",
             "Kirilov ceded the presidency to Shatov because he was less popular",
             "Dan had to stop Bill from toying with the injured bird, he was very compassionate"]

#fHandle = open('out.txt','w')
for sent in sentences:
    query = []
    tags = nltk.pos_tag(nltk.word_tokenize(sent))
    for i,j in tags:
        if j in ['VB','VBD','VBG', 'JJ','RB']:
            print i+" "
    print '\n'