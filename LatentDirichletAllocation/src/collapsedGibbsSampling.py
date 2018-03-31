'''
Created on Mar 9, 2014

@author: Anirudh
'''
import numpy as np
import Tokenize
import nltk

class lda:
    def __init__(self, inputFile, alpha, beta, KTopics, vocab):
        self.corpus = self.loadCorpus(inputFile)
        self.vocab = vocab
        self.alpha = alpha
        self.beta = beta
        self.K = KTopics
        
        for i,doc in enumerate(self.corpus):
            docTerms = Tokenize.tokenizeText(doc)
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
        
    def loadCorpus(self, *inputFile):
        """
        Takes a input as a file with different documents in different lines of the file.
        It returns a list of each of these documents.
        If no input file is given, it takes the nltk brown corpus as the input
        """
        if True:
            fHandle = open(inputFile[0],'r')
            corpus = []
            text = fHandle.read()
            text = text.split('\n')
            for i in text:
                if len(i.split(' ')) < 20:
                    continue
                else:
                    corpus.append(i)
            return corpus[:1000]   
    
    def uniformDirichlet(self, alpha, k):
        priors = [alpha for i in range(k)]
        return np.random.dirichlet(priors,1)
    
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
        for w in range(self.N):
            self.Phi[:,w] = (self.phi[:, w] + self.beta) / (self.wordCount_k + (self.beta*self.N))
            
        for d in range(self.D):
            self.Theta[d] = ((self.theta[d] + self.alpha)/ (sum(self.theta[d]) + (self.alpha*self.K))) 
            
        np.savetxt('E:/Dev/Python/Workspace/LDA/output/Topic-Word-Distribution.txt', self.Phi, delimiter='\t', fmt='%f')
        np.savetxt('E:/Dev/Python/Workspace/LDA/output/Document-Topic-Distribution.txt', self.Theta, delimiter='\t', fmt='%f')
        
    def printTopics(self, numberOfWords):
        phi = np.genfromtxt(open('E:/Dev/Python/Workspace/LDA/output/Topic-Word-Distribution.txt','r'), delimiter='\t', dtype='f8')
        output = ""
        for i,topic in enumerate(phi):
            output = output + "Topic %s : "%i
            wordIndex = sorted(range(len(topic)), key=lambda k: topic[k], reverse=True)[:numberOfWords]
            for i in wordIndex:
                output = output + self.vocab[i] + ", "
            output = output + "\n"   
        
        file = open('E:/Dev/Python/Workspace/LDA/output/Topics.txt','w')
        file.write(output)
        
if __name__ == "__main__":
    mylda = lda('E:/Dev/Python/Workspace/LDA/data/newsCorpus.txt',0.8,0.5,8,[])
    for i in range(75):
        print "Completed iteration %f" %i
        mylda.gibbsSampling()
        
    mylda.saveParameters()
    mylda.printTopics(15)
    '''bagOfWords = mylda.corpus # returns every document as a string indexed by docID
    
    #Replacing the document in the dictionary with the bag of Words 
    for i in bagOfWords:
        bagOfWords[i] = Tokenize.tokenizeText(bagOfWords[i])
    
    for i in bagOfWords:
        mylda.vocab = mylda.vocab + (bagOfWords[i]).keys()
    
    vocab = list(set(mylda.vocab))
    print len(vocab)'''
    
    
    
    '''
    # Document word matrix and singular value decomposition
    docWords = np.zeros((len(vocab),len(bagOfWords)))
    for i in range(len(vocab)):
        for j in range(len(bagOfWords)):
            if vocab[i] in bagOfWords[j]:
                docWords[i][j] = (bagOfWords[j])[vocab[i]] 
            
    print docWords[vocab.index('government')]
    u,s,v = np.linalg.svd(docWords, False, True)
    print u.shape,v.shape''' 