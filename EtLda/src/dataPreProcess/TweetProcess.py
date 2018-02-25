'''
Created on Jun 13, 2014

@author: Anirudh
'''
import re 

fHandle = open('E:/Dev/Python/Workspace/LDA/data/coloradodebate.txt','r')
fOut = open('E:/Dev/Python/Workspace/LDA/data/tweetOut.txt','a')
fOut.truncate()
tweet = fHandle.readline()
'''
tweet = fHandle.readline()
#print tweet
tweet = "Elisa Tinsley - RT @rajunarisetti: Remarkable opinion shift. New WSJ/NBC Poll: Majority Favors One-Party Control http://t.co/I6bxcC2j @WSJ #election2012 ... - Tue Oct 02 17:16:07 EDT 2012"
tweet = "A Progressive Troll - @jimmerz28: Why aren't @jillstein2012 and @GovGaryJohnson in the #DenverDebate? Cause America is unbiased and free. - Tue Oct 02 17:13:31 EDT 2012"
print tweet
tweet = tweet[tweet.find('-')+1:]
newText = re.sub(r'(- Tue.*)|(- Wed.*)|(- Thu.*)',' ', tweet)
newText = re.sub(r'(http[a-z|A-Z|0-9|/|.|:]*)','', newText)
newText = re.sub(r'(- Tue.*\b)',' ', newText)
newText = newText.replace('RT','')
newText = re.sub(r'(@[A-Za-z0-9]+)',' ', newText)
newText = re.sub(r'[^\\bA-Za-z\\b]',' ', newText)
newText = re.sub(r'[ ]+',' ', newText)
if(len(newText) > 3):
    print newText.strip()
'''

while True:
    newText = tweet[tweet.find('-')+1:]
    newText = re.sub(r'(- Tue.*)|(- Wed.*)|(- Thu.*)',' ', newText)
    newText = re.sub(r'(http[a-z|A-Z|0-9|/|.|:]*)',' ', newText)
    newText = newText.replace('RT','')
    newText = re.sub(r'(@[A-Za-z0-9]+)',' ', newText)
    newText = re.sub(r'[^A-Za-z\s]',' ', newText)
    newText = re.sub(r'(\bA-Za-z\b)','', newText)
    newText = re.sub(r'[ ]+',' ', newText).lower()
    if len(newText)>3:
        fOut.write(newText)
    tweet = fHandle.readline()
    if tweet==None or tweet=="":
        break
fHandle.close()
fOut.close()

'''
query = raw_input ( 'Query: ' )
query = urllib.urlencode ( { 'q' : query } )
print query
response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
json = m_json.loads ( response )
results = json [ 'responseData' ] [ 'results' ]
for result in results:
    title = result['title']
    url = result['url']   # was URL in the original and that threw a name error exception
    print ( title + '; ' + url )
'''