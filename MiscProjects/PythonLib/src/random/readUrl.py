'''
Created on May 17, 2014

@author: Anirudh
'''
import urllib2

url = "http://anirudhacharya89.wordpress.com/2013/04/13/reviews-of-india-after-gandhi-book/"
import urllib

search_criteria = raw_input("Insert Google search here: ")
webPage = urllib.FancyURLopener({})
readWeb = webPage.open("http://www.google.com/search?hl=en&q="+search_criteria+"&btnG=Search")
print readWeb.read()