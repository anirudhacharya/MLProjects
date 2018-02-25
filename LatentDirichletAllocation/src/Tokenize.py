'''
Created on Jan 2, 2014

@author: Anirudh
'''
import re
from nltk.corpus import stopwords

def tokenizeText(text):
    """
    Removes stop words, removes non character data and returns a list containing bag of words.
    """
    newText = re.sub(r'[^A-Za-z\s]',' ', text)# removes any numbers or noncharacter info from the string
    newText = re.sub(r'\s+', ' ', newText) # replaces multiple spaces with a single space
    newText = (re.sub(r'\s', '\n', newText)).lower() # replaces spaces with new lines
    tokens = newText.split('\n')
    dictTok = {}
    
    for i in tokens:
        if i in stopwords.words('english'):
            tokens.remove(i)
        
    for i in tokens:
        if len(i) <= 1:
            tokens.remove(i)
        
    for i in tokens:
        if i in dictTok:
            dictTok[i] = dictTok[i] + 1
        else:
            dictTok[i] = 1
            
    return tokens
    
if __name__ == '__main__':
    fHandle = open('newsCorpus.txt','r')
    text = fHandle.readline()
    fHandle.close()
    
    dictTok = tokenizeText(text)
    #test = nltk.word_tokenize(text.lower())
    
    fHandle = open('tokens.txt','w')
    for w in sorted(dictTok, key = dictTok.get, reverse=True):
        #print w, dictTok[w]
        fHandle.write(w+" "+str(dictTok[w]))
        fHandle.write('\n')
    fHandle.close()