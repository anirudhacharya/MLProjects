'''
Created on Jul 7, 2014

@author: Anirudh
'''
import urllib2
import urllib
import json as m_json

for i in range(1):
    query = "cars"+str(i)#raw_input ( 'Query: ' )
    query = urllib.urlencode ( { 'q' : query } )
    print 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query
    '''
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    print results[0]['content']
    print i
    '''