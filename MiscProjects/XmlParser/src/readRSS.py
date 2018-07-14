'''
Created on Jun 29, 2013

@author: AAACHARY
'''
import urllib2 as ulib
from xml.dom import minidom, Node
#http://blog.sushovan.de
#http://anirudhacharya89.wordpress.com
def getFeeds(blogUrl, feedsDict):
    """
    given a blog url and a dictionary, the function updates the dictionary with
    the feed information of the blog url
    """
    urlInfo = str(ulib.urlopen(blogUrl).read())
    rssStartIndex = urlInfo.find("http",urlInfo.find('rss'))
    feedUrl = urlInfo[rssStartIndex:urlInfo.find('"',rssStartIndex+1)]
    feedInfo = str(ulib.urlopen(feedUrl).read())
    
    xmlDoc = minidom.parseString(feedInfo)
    rootNode = xmlDoc.documentElement
    itemNodes = xmlDoc.getElementsByTagName('item')
    titles = xmlDoc.getElementsByTagName('title')
    links = xmlDoc.getElementsByTagName('link')
    desc = xmlDoc.getElementsByTagName('description')
    feedsDict = {}
    postDict = {}
    i = 1
    while i < len(titles):
        postDict[titles[i].childNodes[0].nodeValue] = [links[i].childNodes[0].nodeValue, desc[i].childNodes[0].nodeValue]
        i = i+1 
        
    feedsDict[titles[0].childNodes[0].nodeValue] = postDict
    print feedsDict[titles[0].childNodes[0].nodeValue]
    
if __name__ == '__main__':
    feedsDict = {}
    blogUrl = 'http://anirudhacharya89.wordpress.com'
    getFeeds(blogUrl, feedsDict)