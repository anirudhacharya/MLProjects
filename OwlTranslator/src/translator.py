'''
Created on Mar 18, 2014

@author: Anirudh
'''

import urllib2 as ulib
from xml.dom import minidom, Node
import unicodedata
individualNames =[]
individualNodes = []
classNames = []
classNodes = []
propertyNames = []
propertyNodes = []
fout = open('out.txt','a')

def main():
    fHandle = open('minipizza.owl','r')
    feedInfo = fHandle.read()
    fout.truncate()
    fout.write("%file out.txt")
    fout.write('\n')
    xmlDoc = minidom.parseString(feedInfo)
    individualNames,individualNodes = getIndividuals(xmlDoc)
    str = "objects("
    for i in individualNames:
        str = str+i+";"
    str = str[:-1]+")."
    fout.write(str)
    fout.write('\n \n')
    classNames,classNodes = getOwlClasses(xmlDoc)
    propertyNames,propertyNodes = getObjectProp(xmlDoc)
    generateChoiceRules(xmlDoc)
    generateABox(xmlDoc)
    generateTBox(xmlDoc)

def getIndividuals(xmlDoc):
    individuals = xmlDoc.getElementsByTagName('NamedIndividual') + xmlDoc.getElementsByTagName('owl:NamedIndividual')
    for i,item in enumerate(individuals):
        if item.parentNode.tagName=='rdf:RDF':
            individualNodes.append(item)
            temp = item.attributes.items()[0][1]
            individualNames.append(getPredicate(temp))
    return individualNames,individualNodes

def getOwlClasses(xmlDoc):
    classes = xmlDoc.getElementsByTagName('Class') + xmlDoc.getElementsByTagName('owl:Class')
    newClasses = []
    curClassNodes = []
    for i,item in enumerate(classes):
        if item.parentNode.tagName=='rdf:RDF':
            if item.attributes:
                classNodes.append(item)
                temp = item.attributes.items()[0][1]
                classNames.append(getPredicate(temp))
    return classNames, classNodes
    
def getObjectProp(xmlDoc):
    props = xmlDoc.getElementsByTagName('ObjectProperty') + xmlDoc.getElementsByTagName('owl:ObjectProperty')
    for i,item in enumerate(props):
        if item.parentNode.tagName=='rdf:RDF':
            propertyNodes.append(item)
            temp = item.attributes.items()[0][1]
            propertyNames.append(getPredicate(temp))
            
    return propertyNames,propertyNodes

def generateChoiceRules(xmlDoc):
    for uPred in classNames:
        fout.write("{"+uPred+"(I3):objects(I3)}. \n")
    for bPred in propertyNames:
        fout.write("{"+bPred+"(I3,I4):objects(I3;I4}. \n")
    fout.write('\n')
    return

def generateABox(xmlDoc):    
    '''
    Write down the ABox rules for each individual, by iterating through each of them 
    '''
    for i,item in enumerate(individualNodes):
        children = item.childNodes
        fout.write("% "+individualNames[i]+"\n")
        for child in children:
            if child.localName==None:
                continue
            elif child.localName=='type':
                '''
                If the node is of rdf:type then we define a unary predicate telling that the individual is of type
                the class of the given rdf:type
                '''
                if child.attributes:
                    fout.write(getRdfType(child)+"("+individualNames[i]+"). \n")
                else:
                    print "TODO ABox Individual declaration of unary predicates for complex classes"
            elif child.localName in propertyNames:
                '''
                If the child node is of type owl:<ObjectProperty name> then we define it as an object property of the 
                individual and declare it as a binary predicate in the ABox
                '''
                if child.attributes:
                    fout.write(child.localName+"("+individualNames[i]+","+getRdfType(child)+"). \n")
                else:
                    print "TODO ABox Individual declaration of binary predicates for complex classes"
        fout.write('\n')    
    return

def generateTBox(xmlDoc):
    '''
    Generate the TBox rules to get the constraints in the ontology.
    '''
    for i,item in enumerate(classNodes):
        classA = getRdfType(item)
        children = item.childNodes
        for child in children:
            if child.localName==None:
                continue
            elif child.localName=='subClassOf':
                fout.write("![Z0]: ("+classA+"(Z0) -> "+subClassOf(child,0)+". \n")
        fout.write('\n')
    
    for i,item in enumerate(propertyNodes):
        children = item.childNodes
        for child in children:
            nodeType = child.localName
            if nodeType == 'domain':
                if child.attributes:
                    fout.write("![Z,Z1]: ("+propertyNames[i]+"(Z,Z1) -> "+getRdfType(child)+"(Z)). \n")
                else:
                    print "TODO expand domain class"
            elif nodeType == 'range':
                if child.attributes:
                    fout.write("![Z,Z1]: ("+propertyNames[i]+"(Z,Z1) -> "+getRdfType(child)+"(Z1)). \n")
                else:
                    print "TODO expand range class"
            elif nodeType == 'inverseOf':
                if child.attributes:
                    fout.write("![Z,Z1]: ("+propertyNames[i]+"(Z,Z1) -> "+getRdfType(child)+"(Z1,Z)). \n")
                else:
                    print "TODO expand inverseOf class"
            elif nodeType == 'subPropertyOf':
                if child.attributes:
                    fout.write("![Z,Z1]: ("+propertyNames[i]+"(Z,Z1) -> "+getRdfType(child)+"(Z,Z1)). \n")
                else:
                    print "TODO expand subPropertyOf class"
            fout.write('\n')
    
    '''Printing the disjoint rule'''
    desc = xmlDoc.getElementsByTagName('rdf:Description')
    for i,item in enumerate(desc):       
        if item.parentNode.tagName != 'rdf:RDF':
            desc.pop(i)
    
    for i,item in enumerate(desc):
        for j,child in enumerate(item.childNodes):
            
            if getRdfType(child) == 'allDisjointClasses':
                children = child.childNodes
                memNodes = child.parentNode.getElementsByTagName('members')
                for mem in memNodes:
                    collNodes = [getRdfType(m) for m in mem.getElementsByTagName('rdf:Description')]
                for disjointNode1 in collNodes:
                    for disjointNode2 in collNodes:
                        if disjointNode1 != disjointNode2:
                            fout.write("![Z]: ("+disjointNode1+"(Z) -> not "+disjointNode2+"(Z)).\n")
                fout.write("\n")
                #mem = memNode.children   
    return

def subClassOf(classB,count):
    '''
    defines a rule telling classA is subclass of classB
    '''
    if classB.attributes:
        classBName = getRdfType(classB)
        return classBName+"(Z"+str(count)+")"
    else:
        restriction = classB.getElementsByTagName('Restriction')
        print [r.firstChild.nextSibling.toxml() for r in restriction]
        #print getRdfType(restriction.firstChild)
        #print "TODO subclass of complex classes(restriction etc..)" #classB.firstChild.toxml()
    return ""

def getRdfType(node):
    '''
    Given a node it returns the attribute value of the first attribute
    '''
    if node.childNodes != None and node.attributes:
        return getPredicate(node.attributes.items()[0][1])

def getPredicate(link):
    temp = unicodedata.normalize('NFKD', link).encode('ascii','ignore')
    loc = 0
    if temp.find('#')>=0:
        loc = temp.index('#')+1
    elif temp.find(';')>=0:
        loc = temp.index(';')+1
    else:
        loc=0
    temp = temp[loc:]
    temp = temp[0].lower()+temp[1:]
    return temp

if __name__ == '__main__':
    main()