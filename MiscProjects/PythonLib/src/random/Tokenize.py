'''
Created on Jan 2, 2014

@author: Anirudh
'''
import re
def tokenizeText(file):
    fHandle = open(file,'r')
    text = fHandle.readline()
    fHandle.close()
    newText = re.sub(r'[^A-Za-z\s.]',' ', text)# removes any numbers or noncharacter info from the string
    newText = re.sub(r'\s+', ' ', newText) # replaces multiple spaces with a single space
    newText = (re.sub(r'\s', '\n', newText)).lower() # replaces spaces with new lines
    tokens = newText.split('\n')
    dictTok = {}
    for i in tokens:
        if len(i) <= 1:
            tokens.remove(i)
        else:
            if i in dictTok:
                dictTok[i] = dictTok[i] + 1
            else:
                dictTok[i] = 1

    fHandle = open('tokens.txt','w')
    
    for w in sorted(dictTok, key = dictTok.get, reverse=True):
        #print w, dictTok[w]
        fHandle.write(w+" "+str(dictTok[w]))
        fHandle.write('\n')
    fHandle.close()
    return

if __name__ == '__main__':
    tokenizeText('text.txt')