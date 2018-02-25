'''
Created on Dec 1, 2012

@author: AAACHARY
'''
import urllib2
def get_page(url):
    print url
    stuff = str(urllib2.urlopen(url).read())
    fHandle = open('temp.txt','w')
    fHandle.write(stuff) 
    return stuff

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
            
def get_next_target(page):
    start_link = page.find('<a href="http')-5
    if(start_link==-1):
        return None,0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

def get_all_links(page):
    links=[]
    pos=0
    while page:
        url,pos = get_next_target(page)
        if url:
            links.append(url)
            page=page[pos:]
        else:
            break
    return links

def crawl_web(seedLink,maxDepth): #breadth-first crawling
    tocrawl=[seedLink]
    crawled=[]
    index=[]
    next = []
    depth=0
    while tocrawl and depth<=maxDepth:
        pageLink=tocrawl.pop()
        if pageLink not in crawled:
            page = get_page(pageLink)
            union(next,get_all_links(page))
            crawled.append(pageLink);
            add_page_to_index(index,pageLink,page);
            #print(pageLink)
        if not tocrawl:
            tocrawl = next
            next = []
            depth = depth+1
    return index
            
def add_to_index(index,keyword,url):
    # format of the index - [[keyword,[url,url,...]],
    #                       [keyword,[url,url,...]],...]
    
    
    
    flag = 1
    for i in index:
        if(keyword == i[0]):
            if url not in i[1]:
                i[1].append(url)
            flag = 0
            break
        else:
            continue
    if(flag == 1):
        index.append([keyword,[url]])

def lookup(index,keyword):
    for i in index:
        if i[0]==keyword:
            return i[1]
        else:
            continue
    return []

def add_page_to_index(index,url,page):
    for i in page.split():
        add_to_index(index,i,url)    

#page = get_page("http://www.udacity.com/cs101x/index.html")
#index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]
index=crawl_web("http://anirudhacharya89.wordpress.com/2013/04/13/reviews-of-india-after-gandhi-book/",1)
print lookup(index,"Atanu")
#print get_page("http://anirudh2189.wordpress.com/2011/06/07/democracy/")