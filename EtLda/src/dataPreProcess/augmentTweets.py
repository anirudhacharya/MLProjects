'''
Created on May 17, 2014

@author: Anirudh
'''
import urllib2
import urllib
import json as m_json
for i in range(1000):
    query = "cars"+str(i)#raw_input ( 'Query: ' )
    query = urllib.urlencode ( { 'q' : query } )
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    print results[0]['content']
    print i

'''
for result in results:
    title = result['title']
    url = result['url']   # was URL in the original and that threw a name error exception
    print ( title + '; ' + url )'''