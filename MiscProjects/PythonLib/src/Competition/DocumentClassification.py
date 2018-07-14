'''
Created on Sep 9, 2014

@author: Anirudh
'''
import numpy as np
import nltk
from nltk.corpus import stopwords
import re

def main():
    N = int(raw_input())
    data = []
    B = []
    fHandle = open('training.txt','r')
    numTestCases = int(fHandle.readline())
    for i in range(N):
        line = fHandle.readline()
        data.append(line[2:])
        B.append(int(line[:1]))
    mylda = lda(data,0.3,0.1,8,[])
    mylda.gibbsSampling()
    mylda.saveParameters()
    model = LinRegression()
    w = model.getParameters(mylda.Theta, B, 0.1, N, 8)
    return

class lda:
    def __init__(self, inputFile, alpha, beta, KTopics, vocab):
        self.corpus = inputFile
        self.vocab = vocab
        self.alpha = alpha
        self.beta = beta
        self.K = KTopics
        
        for i,doc in enumerate(self.corpus):
            docTerms = self.tokenizeText(doc)
            self.vocab = self.vocab + docTerms
            self.corpus[i] = docTerms
        
        self.vocab = list(set(self.vocab))
        
        self.D = len(self.corpus)
        self.theta = np.zeros((self.D, self.K)) # count of words assigned to topic k in doc D/ n_m_z / n_dk
        
        self.N = len(self.vocab)
        self.phi = np.zeros((self.K, self.N)) # word count of each word in topic K / n_zt / n_kw
        
        self.z_dn = [] # topics of every word in doc D
        self.wordCount_k = np.zeros(self.K) # word count of each topic K
        
        '''
        Initialize a random topic to every word in every document and appropriately change the phi and theta matrices.
        '''
        for i,doc in enumerate(self.corpus):
            z_d = []
            for word in doc:
                z = np.random.randint(0,self.K) # a random topic drawn from the list of K topics
                z_d.append(z)
                '''
                A word has been assigned to topic z in the current doc i. Update the Doc-topic distribution
                '''
                self.theta[i][z] += 1
                '''
                The word 'word' has been assigned to topic z. So update the topic-word dist 
                '''
                self.phi[z][(self.vocab).index(word)] += 1
                '''
                The word count of topic z has to be incremented.
                '''
                self.wordCount_k[z] += 1
            
            z_d = np.array(z_d)
            self.z_dn.append(z_d)
        
        self.Phi = np.zeros(self.phi.shape)
        self.Theta = np.zeros(self.theta.shape)
        
    def tokenizeText(self,text):
        """
        Removes stop words, removes non character data and returns a list containing bag of words.
        """
        newText = re.sub(r'[^A-Za-z\s]',' ', text)# removes any numbers or noncharacter info from the string
        newText = re.sub(r'\s+', ' ', newText) # replaces multiple spaces with a single space
        newText = (re.sub(r'\s', '\n', newText)).lower() # replaces spaces with new lines
        tokens = newText.split('\n')
        dictTok = {}
    
        for i in tokens:
            if i in stopwords.words('english'):
                tokens.remove(i)
        
        for i in tokens:
            if len(i) <= 1:
                tokens.remove(i)
        
        for i in tokens:
            if i in dictTok:
                dictTok[i] = dictTok[i] + 1
            else:
                dictTok[i] = 1
            
        return tokens
    
    def gibbsSampling(self):
        for d,doc in enumerate(self.corpus):
            #print "Sampling Document %f" %d
            z_d = self.z_dn[d]
            
            for w,word in enumerate(doc):
                cur_z = z_d[w] # get currently assigned topic
                wt = (self.vocab).index(word) # index of the word in the vocabulary
                
                '''
                discount the current assignent from the matrices
                '''
                self.theta[d][cur_z] -= 1
                self.phi[cur_z][wt] -= 1
                self.wordCount_k[cur_z] -= 1
                
                '''
                get new topic assignment
                '''
                probabilityTopics = ((self.phi[:, wt] + self.beta) 
                                     / (self.wordCount_k + (self.beta*self.N))) * ((self.theta[d] + self.alpha)
                                                                                   / (sum(self.theta[d]) 
                                                                                      + (self.alpha*self.K)))
                newTopic = np.random.multinomial(1, probabilityTopics / probabilityTopics.sum()).argmax()
                '''
                update the matrices with the new topic assignment
                '''
                z_d[w] = newTopic
                self.theta[d][newTopic] += 1
                self.phi[newTopic][wt] += 1
                self.wordCount_k[newTopic] += 1
        return
    
    def saveParameters(self):
        #for w in range(self.N):
        #   self.Phi[:,w] = (self.phi[:, w] + self.beta) / (self.wordCount_k + (self.beta*self.N))
            
        for d in range(self.D):
            self.Theta[d] = ((self.theta[d] + self.alpha)/ (sum(self.theta[d]) + (self.alpha*self.K))) 
            
        #np.savetxt('E:/Dev/Python/Workspace/LatentDirichletAllocation/output/Topic-Word-Distribution.txt', self.Phi, delimiter='\t', fmt='%f')
        #np.savetxt('E:/Dev/Python/Workspace/LatentDirichletAllocation/output/Document-Topic-Distribution.txt', self.Theta, delimiter='\t', fmt='%f')
        
    def printTopics(self, numberOfWords):
        phi = np.genfromtxt(open('E:/Dev/Python/Workspace/LatentDirichletAllocation/output/Topic-Word-Distribution.txt','r'), delimiter='\t', dtype='f8')
        output = ""
        for i,topic in enumerate(phi):
            output = output + "Topic %s : "%i
            wordIndex = sorted(range(len(topic)), key=lambda k: topic[k], reverse=True)[:numberOfWords]
            for i in wordIndex:
                output = output + self.vocab[i] + ", "
            output = output + "\n"   
        
        file = open('E:/Dev/Python/Workspace/LatentDirichletAllocation/output/Topics.txt','w')
        file.write(output)
        
class LinRegression:
    def __init__(self):
        return
    
    def getParameters(self, A, B, alpha, N, F):
        w = np.ones(F+1)
        h = np.dot(w,A.T)
        J = sum((h-B)**2)/(2*N)
        Jval = []
        Jval.append(J)
        while True:
            dJ = (h - B)/N
            for i in range(F+1):
                w[i] = w[i] - alpha*sum(dJ * A[:,i])    
        
            prevJ = J
            h = np.dot(w,A.T)
            J = sum((h-B)**2)/(2*N)  
            Jval.append(J)  
            if abs(J-prevJ)<0.0001:
                break
        
        return w
    
    def solve(self, w, test, T):
        for i in range(T):
            y = np.dot(w,test.T)
        return y

if __name__ == '__main__':
    main()