'''
Created on Jun 13, 2014

@author: Anirudh
'''
import re
from nltk.corpus import stopwords
import numpy as np
import random

class EtLda:
    def __init__(self, alpha_delta, alpha_gamma, alpha_lambda, alpha_theta, alpha_psi, beta, gamma, delta, psi, 
                 theta, KTopics):
        self.vocab = []
        self.K = KTopics
        self.trans = self.loadTranscript('E:/Dev/Python/Workspace/LDA/data/etldaTrans')
        self.tweets = self.loadTweets('E:/Dev/Python/Workspace/LDA/data/tweetOut.txt')
        
        self.alpha_delta = alpha_delta
        self.alpha_gamma = alpha_gamma
        self.alpha_lambda = alpha_lambda
        self.alpha_theta = alpha_theta
        self.alpha_psi = alpha_psi
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.psi = psi
        self.theta = theta
        self.c_s = 1
        self.c_t = 1
        
        '''
        Initialize the arrays that hold the count values
        '''
        self.N = len(self.vocab)
        self.S = len(self.trans)
        self.T = len(self.tweets)
        self.phiK = np.zeros((self.K, self.N)) # Count of each word in each of the topics
        self.thetaS = np.zeros((self.S, self.K)) # list of distributions of the different segments. 
                                                    #Count of words in seg S
        self.general = np.zeros((1,self.K)) # generalised distribution
        self.z_sn = []
        self.z_tn = []
        self.segInd = np.zeros(self.S)
        self.distInd = np.zeros(self.T)
        self.coRefInd = []
        # Intialize
        '''
        each line is a paragraph, assign a segment indicator drawn from a binomial distribution
        '''
        self.S1 = 0 # number of segments
        for i in range(self.S):
            if random.random()<0.9:
                self.segInd[i] = 0
            else:
                self.segInd[i] = 1
                self.S1+=1
        '''
        Assign a topic for each word in the transcript
        '''
        for para in self.trans:
            z_s = []
            for word in para:
                tempZ = random.choice(range(self.K))
                z_s.append(tempZ)
                self.phiK[tempZ][word] += 1
            self.z_sn.append(z_s) 
        
        '''
        For each tweet assign a topic indicator - general or specific 
        '''
        for tweet in self.tweets:
            self.distInd.append(random.random([0,1]))
            '''
            IF it is a specific topic assign a segment indicator
            '''
            if id == 0:
                self.coRefInd.append(random.choice(range(self.S1)))
        
            '''
            Assign a topic to each word from the distribution
            '''
            z_t = []
            for word in tweet:
                z_t.append(random.choice(range(self.K)))
            self.z_tn.append(z_t)
            
        # Gibbs Sampling
            
        return
    
    def loadTranscript(self, inputFile):
        """
        Takes a input as a file with different documents in different lines of the file.
        It returns a list of each of these documents.
        """
        fHandle = open(inputFile,'r')
        corpus = []
        text = fHandle.read()
        text = re.sub(r'[^A-Za-z\s]',' ', text)# removes any numbers or noncharacter info from the string
        text = re.sub(r'[ ]+', ' ', text).lower() # replaces multiple spaces with a single space
        text = text.split('\n')
        corpus = []
        for line in text:
            tokens = self.getTokens(line)
            if len(tokens) < 20:
                corpus[-1] = corpus[-1] + tokens
            else:
                corpus.append(tokens)
        # End of line for loop
        return corpus
    
    def loadTweets(self, inputFile):
        """
        Takes a input as a file with different documents in different lines of the file.
        It returns a list of each of these documents.
        ***
        corpus = []
        with open(inputFile,'r') as fHandle:
            line = fHandle.readlines()
            tokens = self.getTokens(line)
            corpus.append(tokens)

        return corpus
        """
        fHandle = open(inputFile,'r')
        corpus = []
        text = fHandle.read()
        text = text.split('\n')
        text = text[:5000]
        corpus = []
        for line in text:
            tokens = self.getTokens(line)
            corpus.append(tokens)
        # End of line for loop
        return corpus
    
    def getTokens(self, line):
        line = line.split(' ')
        tokens = []
        for word in line:
            if word not in stopwords.words('english'):
                if len(word) > 1:
                    try:
                        pos = self.vocab.index(word)
                        tokens.append(pos)
                    except:
                        tokens.append(len(self.vocab))
                        self.vocab.append(word)  
        #End of Word for loop
        return tokens
    
    def gibbsSampling(self):
        return
        
my = EtLda(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
print len(my.tweets)
print my.tweets[100]
#fOut = open('vocab','w')
#fOut.write("\n".join(my.vocab))