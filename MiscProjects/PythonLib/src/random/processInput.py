'''
Created on Nov 29, 2013

@author: Anirudh
'''
import numpy as np
import re
from pymongo import MongoClient

client = MongoClient()
db = client['tweetDB']
collection = db['twitterSearch']

denDeb = db.DenverDebate
fHandle = open('E:/Dev/Python/Workspace/EtLda/data/coloradodebate.txt','r') #open('temp','r')#
fOut = open('tweetOut.txt','a')
fOut.truncate()
temp = fHandle.read()
#x = re.findall(r'(^.*?)-|- (.*?)- [Tue|Wed|Thur]',temp, re.MULTILINE | re.DOTALL)
x = re.findall(r'(^.*?)- (.*?)- (.*?$)',temp, re.MULTILINE | re.DOTALL)
print x[0][2].strip()
'''
for i,t in enumerate(x):
    #newText = re.sub(r'\n',' ', t)
    print t
    #newText = re.sub(r'(http[a-z|A-Z|0-9|/|.|:]*)',' ', newText)
    #newText = newText.replace('RT','')
    #newText = re.sub(r'(@[A-Za-z0-9]+)',' ', newText)
    #newText = re.sub(r'[^A-Za-z\s]',' ', newText)
    #newText = re.sub(r'(\b(\w)\b)','', newText)
    #newText = re.sub(r'[ ]+',' ', newText).lower()
    #fOut.write(newText.strip()+"\n")
''' 
fOut.close()
fHandle.close()