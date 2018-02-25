'''
Created on Jun 20, 2014

@author: Anirudh
'''
import re
import Tokenize
fHandle = open('E:/Dev/Python/Workspace/LDA/data/etldaTranscript')
fOut = open('E:/Dev/Python/Workspace/LDA/data/etldaTrans','a')
fOut.truncate()
i=1
exList = ['obama','romney','lehrer','mr','president']
with open('E:/Dev/Python/Workspace/LDA/data/etldaTranscript') as fHandle:
    for line in fHandle:
        if i%2==1:
            #newText = re.sub(r'[^A-Za-z\s]',' ', line)# removes any numbers or noncharacter info from the string
            #newText = (re.sub(r'\s+', ' ', newText)).lower() # replaces multiple spaces with a single space
            #newText = (re.sub(r'\s', '\n', newText)).lower() # replaces spaces with new lines
            fOut.write(line)
            print line
        i += 1

'''
transcript = []
exList = ['obama','romney','lehrer','mr','president']
with open('E:/Dev/Python/Workspace/LDA/data/etldaTrans') as fHandle:
    for line in fHandle:
        words = line.split(' ')
        for i,word in enumerate(words):
            words[i] = word.lower()
            if word in exList:
                words.remove(word)
                word = re.sub(r'[^A-Za-z\s]','', word)
        transcript.append(words)
'''