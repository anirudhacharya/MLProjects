'''
Created on Apr 16, 2014

@author: Anirudh
'''
import urllib2 as ulib
from xml.dom import minidom, Node
import unicodedata

fHandle = open('tempin','r')
feedInfo = fHandle.read()
    
xmlDoc = minidom.parseString(feedInfo)

root = xmlDoc.documentElement
owlClasses = root.getElementsByTagName('Restriction')
#owlClasses = root.getElementsByTagName('owl:ObjectProperty')
#print (owlClasses[0].childNodes)[3].toxml()
owlClass = owlClasses[0]
#print owlClass.attributes.items()

for node in owlClass.childNodes:
    if node.attributes:
        temp = node.attributes.items()[0][1]
        temp = unicodedata.normalize('NFKD', temp).encode('ascii','ignore')
        print temp[temp.index('#')+1:]
'''

for owlClass in owlClasses:
    if owlClass.attributes:
        temp = owlClass.attributes.items()[0][1]
        print unicodedata.normalize('NFKD', temp).encode('ascii','ignore')
'''