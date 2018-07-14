import urllib2 as ul
f = ul.urlopen("http://anirudhacharya89.wordpress.com/2014/04/07/absurdity-of-opposing-dynasty-politics/",timeout=10)
print f.read()
