# A node of the trie
class Node():
    # Constructor
    # Sets string and initializes a dictionary which maintains child node mappings
    def __init__(self,string):
        self.string=string
        self.dict={} # Maps an edge (specified by a character) to a child node

    # -> String
    # Gets the string of a node
    def getString(self):
        return self.string

    # -> Dictionary
    # Gets the dict of a node
    def getDict(self):
        return self.dict

    # Character Node ->
    # Sets the child node connected via an edge specified by char
    def setNext(self,char,aNode):
        self.dict[char]=aNode

    # Character -> Node/None
    # Gets the child node connected via edge specified by char
    def getNext(self,char):
        if (char in self.dict):
            return self.dict[char]

    # -> String
    # String form of a node
    def __str__(self):
        resultString = self.string
        if(not self.dict.keys()):
            return resultString
        resultString=resultString + "\nConnected to: "
        for char in self.dict.keys():
            resultString = resultString + char + "\t"
        return resultString

    # A trie structure
class Trie():
# Constructor
# Consumes a list of strings a constructs a corresponding trie
    def __init__(self,words):
        self.startNode=Node("")
        for word in words:
            currNode=self.startNode
            for char in word:
                prevNode=currNode
                if(not prevNode.getNext(char)):
                    currNode=Node(prevNode.getString()+char)
                    prevNode.setNext(char,currNode)
                else:
                    currNode=prevNode.getNext(char)

                # String -> Boolean
    # Returns whether string is present in the trie
    def wordStartsWith(self,string):
        currNode=self.startNode
        for letter in string:
            if(not currNode.getNext(letter)):
                return False
            else:
                currNode=currNode.getNext(letter)
        return True