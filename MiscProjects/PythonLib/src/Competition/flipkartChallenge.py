'''
Created on Jun 24, 2014

@author: Anirudh
'''

from nltk.corpus import stopwords
import re

stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'yo', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now','paperback','edition','hardcover','nd','st']
def tokenizeText(text):
    """
    Removes stop words, removes non character data and returns a list containing bag of words.
    """
    text = re.sub(r'[^A-Za-z\s]',' ', text)# removes any numbers or noncharacter info from the string
    text = re.sub(r'\s+', ' ', text).lower() # replaces multiple spaces with a single space
    text = text.split(' ')
    tokens = set()
    for i in text:
        if i not in stopwords:
            if len(i)>1:
                tokens.add(i)
     
    return tokens

N = int(raw_input())
bookName = []
bookDesc = []
for i in range(N):
    bookName.append((tokenizeText(raw_input()),i+1))

dummy = raw_input()

for i in range(N):
    bookDesc.append(tokenizeText(raw_input()))

for i,desc in enumerate(bookDesc):
    notPrinted = True
    lowTuple = (2,bookName[0])
    for j,name in enumerate(bookName):
        diff = name[0].difference(desc)
        if len(diff) <= (len(name[0])*0.15):
            print name[1]
            bookName.remove(name)
            notPrinted = False
            break
        else:
            factor = len(diff)/len(name[0])
            if factor<=lowTuple[0]:
                lowTuple = (factor,(name[0],name[1]))
    if notPrinted:
        print lowTuple[1][1]
        bookName.remove(lowTuple[1])
        
'''
from nltk.corpus import stopwords
import re

def tokenizeText(text):
    """
    Removes stop words, removes non character data and returns a list containing bag of words.
    """
    text = re.sub(r'[^A-Za-z\s]',' ', text)# removes any numbers or noncharacter info from the string
    text = re.sub(r'\s+', ' ', text).lower() # replaces multiple spaces with a single space
    text = text.split(' ')
    tokens = set()
    for i in text:
        if i not in stopwords.words('english')+['paperback','edition','hardcover','nd','st']:
            if len(i)>1:
                tokens.add(i)
     
    return tokens

N = int(raw_input())
bookName = []
bookDesc = []
for i in range(N):
    bookName.append((tokenizeText(raw_input()),i+1))

print bookName
dummy = raw_input()

for i in range(N):
    bookDesc.append(tokenizeText(raw_input()))
printCount = 0
for i,desc in enumerate(bookDesc):
    notPrinted = True
    lowTuple = (2,bookName[0])
    for j,name in enumerate(bookName):
        diff = name[0].difference(desc)
        if len(name)<=5:
            if len(diff)<=3:
                print name[1]
                printCount+=1
                bookName.remove(name)
                notPrinted = False
                break
        elif len(diff) <= (len(name[0])*0.25):
            print name[1]
            printCount+=1
            bookName.remove(name)
            notPrinted = False
            break
        else:
            factor = len(diff)/len(name[0])
            if lowTuple[0]>=factor:
                lowTuple = (factor,(name[0],name[1]))
    if notPrinted:
        print lowTuple[1][1]
        bookName.remove(name)
        
print "sasdsdsd"+str(printCount)
'''