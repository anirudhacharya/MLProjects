'''
Created on Jun 13, 2014

@author: Anirudh
'''
import re
from nltk.corpus import stopwords
import numpy as np
import random

class EtLda:
    #alpha_delta=0.1, alpha_gamma=0.1, alpha_lambda=[0.5,0.5], alpha_theta=0.1, alpha_psi=0.1, beta=0.01, KTopics=10
    def __init__(self, alpha_delta, alpha_gamma, alpha_lambda, alpha_theta, alpha_psi, beta, KTopics):
        self.vocab = []
        self.K = KTopics
        self.trans = self.loadTranscript('E:/Dev/Python/Workspace/EtLDA/data/etldaTrans1')
        self.tweets = self.loadTweets('E:/Dev/Python/Workspace/LDA/data/tweetOut.txt')
        
        self.alpha_delta = alpha_delta
        self.alpha_gamma = alpha_gamma
        self.alpha_lambda = alpha_lambda
        self.alpha_theta = alpha_theta
        self.alpha_psi = alpha_psi
        self.beta = beta
              
        '''
        Initialize the arrays that hold the count values
        '''
        self.N = len(self.vocab)
        self.S = len(self.trans)    # number of segments
        self.T = len(self.tweets)
        
        self.n_sw = np.zeros((self.K, self.N)) # Topic-Word Count for the event
        self.n_tw = np.zeros((self.K, self.N)) # Topic-Word Count for the tweets
        self.n_ik = np.zeros((self.K))    # generalised Topic distribution n_ki
        
        self.n_sk = np.zeros((self.S, self.K))     # Segment-Topic distribution for event
        self.nt_sk = np.zeros((self.S, self.K))    # Tweet-Topic Distribution for tweets
        self.M = np.zeros((self.T,2))           # Count of General and Specific words in a particular tweet 
                                                # 0 is specific topic and 1 is general topic
                                                
        self.n_is = np.zeros((self.S,self.T))   # number of words refer to segment s in tweet t.
        
        self.segChoiceInd = []                  # segment Choice indicator for the specific words of tweets, 
                                                # general words have -1 values
                
        self.z_sn = []
        self.z_tn = []
        
        # Intialize
        '''
        each line is a paragraph, assign a segment indicator drawn from a binomial distribution
        
        self.S1 = 0 # number of segments
        for i in range(S):
            if random.random()<0.9:
                self.segInd[i] = 0
            else:
                self.segInd[i] = 1
                S1+=1
        '''
        '''
        Assign a topic for each word in the transcript
        '''
        
        for s,segment in enumerate(self.trans):
            z_s = []
            for word in segment:
                tempZ = random.choice(range(self.K))    # choose a random topic for the current word from the K topics
                z_s.append(tempZ)
                ''' Modify the count matrices appropriately '''
                self.n_sw[tempZ][word] += 1     # Topic tempz has one more word under the word 'word'
                self.n_sk[s][tempZ] += 1           # Segment i has one more word under topic tempz  
            self.z_sn.append(z_s)                    # append the topic assignment values to the list z_sn
        
        '''
        For each tweet assign a topic indicator - general or specific 
        '''
        for i,tweet in enumerate(self.tweets):
            z_t = []
            segInd = []
            for word in tweet:
                c_t = random.choice([0,1])
                topic = random.choice(range(self.K))
                z_t.append(topic)
                self.n_tw[topic][word] += 1
                if c_t == 1:
                    segInd.append(-1)
                    self.n_ik[topic] += 1
                else:
                    segment = random.choice(range(self.S))
                    segInd.append(segment)
                    self.nt_sk[segment][topic] += 1
                    self.n_is[segment][i] += 1
                    
                self.M[i][c_t] += 1            # General or specific topic indicator, 1 is general 0 is specific
            self.segChoiceInd.append(segInd)  
            self.z_tn.append(z_t)
        
        # Gibbs Sampling    
        return
    
    def loadTranscript(self, inputFile):
        """
        Takes a input as a file with different segments in different lines of the file.
        It returns a list of words ids for each of these segments
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
        tempList = ['obama','president','']
        for word in line:
            if word not in stopwords.words('english'):
                if len(word) > 2:
                    try:
                        pos = self.vocab.index(word)
                        tokens.append(pos)
                    except:
                        tokens.append(len(self.vocab))
                        self.vocab.append(word)  
        #End of Word for loop
        return tokens
    
    def gibbsSampling(self):
        # sample z_s
        for s,segment in enumerate(self.trans):
            z_s = self.z_sn[s]
            for w,word in enumerate(segment):
                curTopic = z_s[w] 
                self.n_sw[curTopic][word] -= 1
                #self.n_tw[curTopic][word] -= 1
                self.n_sk[s][curTopic] -= 1
                #self.nt_sk[s][curTopic] -= 1
                
                newTopicProb = ((self.n_sw[:,word]+self.n_tw[:,word]+self.beta)/
                               (sum(self.n_sw[:,word])+sum(self.n_tw[:,word])+
                                (self.beta*self.N)))*((self.n_sk[s]+ self.nt_sk[s] + 
                                                       self.alpha_theta)/(sum(self.n_sk[s])+
                                                                          sum(self.nt_sk[s])+(self.K*self.alpha_theta)))
                
                try:
                    newTopic = np.random.multinomial(1, newTopicProb / newTopicProb.sum()).argmax()
                except:
                    print "Here"
                
                self.n_sw[newTopic][word] += 1
                #self.n_tw[newTopic][word] += 1
                self.n_sk[s][newTopic] += 1
                #self.nt_sk[s][newTopic] += 1
                z_s[w] = newTopic
            self.z_sn[s] = z_s
        
        for t,tweet in enumerate(self.tweets):
            z_t = self.z_tn[t]
            segInd = self.segChoiceInd[t] 
            for w,word in enumerate(tweet):
                '''discounting the values'''
                curWordSeg = segInd[w]
                curTopic = z_t[w]
                self.n_tw[curTopic][word] -= 1
                if curWordSeg==-1:
                    self.M[t][1] -= 1
                    self.n_ik[curTopic] -= 1
                else:
                    self.M[t][0] -= 1
                    self.nt_sk[curWordSeg][curTopic] -= 1
                    self.n_is[curWordSeg][t] -= 1
                                
                if curWordSeg==-1:      
                    '''
                    General Topic Distribution c_t=1
                    '''
                    topicIndProb = ((self.M[t][1]+self.alpha_lambda[1])/
                                    (sum(self.M[t])+sum(self.alpha_lambda)))*((self.n_ik[curTopic] + self.alpha_psi)/
                                                                    (sum(self.n_ik)+(self.K*self.alpha_psi)))
                    
                    newInd = np.random.binomial(1,topicIndProb)
                    
                    if newInd==1:
                        '''
                        The new distribution is again general.
                        '''
                        self.M[t][1] += 1
                        # sample z_t
                        #self.n_sw[curTopic][word] -= 1
                        #self.n_tw[curTopic][word] -= 1
                        # n_ik has already been discounted
                        
                        newTopicProb = ((self.n_sw[:,word]+self.n_tw[:,word]+self.beta)/
                                    (sum(self.n_sw[:,word])+sum(self.n_tw[:,word])+
                                     (self.beta*self.N)))*((self.n_ik+self.alpha_psi)/(sum(self.n_ik)+
                                                           (self.K*self.alpha_psi)))
                        
                        newTopic = np.random.multinomial(1, newTopicProb / newTopicProb.sum()).argmax()
                        
                        #self.n_sw[newTopic][word] += 1
                        self.n_tw[newTopic][word] += 1
                        self.n_ik[newTopic] += 1
                        
                        z_t[w] = newTopic
                        segInd[w] = -1      # general distribution hence -1 as segment indicator
                        
                    else:
                        '''
                        The new distribution is a specific distribution. So we will have to choose a segment 
                        and then a topic
                        '''
                        self.M[t][0] += 1
                        # sample s_t
                        #self.n_sk[curWordSeg][curTopic] -= 1
                        #self.nt_sk[curWordSeg][curTopic] -= 1
                        #self.n_is[curWordSeg][t] -= 1
                        
                        segProb = ((self.n_sk[:,curTopic]+
                                    self.nt_sk[:,curTopic]+
                                    self.alpha_theta)/(sum(self.n_sk[:,curTopic])+
                                                       sum(self.nt_sk[:,curTopic])+
                                                       (self.K*self.alpha_theta))) *((self.n_is[:,t]+
                                                                                      self.alpha_gamma)/(sum(self.n_is[:,t])+ 
                                                                                     (self.alpha_gamma * self.S)))
                        
                        newSeg = np.random.multinomial(1, segProb / segProb.sum()).argmax()
                        
                        self.n_is[newSeg][t] += 1
                        segInd[w] = newSeg
                        
                        # sample z_t
                        
                        #self.n_sk[curSeg][curTopic] -= 1
                        #self.nt_sk[curSeg][curTopic] -= 1   This has already been done
                
                        newTopicProb = ((self.n_sw[:,word]+self.n_tw[:,word]+self.beta)/
                               (sum(self.n_sw[:,word])+sum(self.n_tw[:,word])+
                                (self.beta*self.N)))*((self.n_sk[newSeg]+ self.nt_sk[newSeg] + 
                                                       self.alpha_theta)/(sum(self.n_sk[newSeg])+
                                                                          sum(self.nt_sk[newSeg])+(self.K*self.alpha_theta)))
                    
                        newTopic = np.random.multinomial(1, newTopicProb / newTopicProb.sum()).argmax()
                        
                        #self.n_sw[newTopic][word] += 1
                        self.n_tw[newTopic][word] += 1
                        #self.n_sk[newSeg][newTopic] += 1
                        self.nt_sk[newSeg][newTopic] += 1
                        
                        z_t[w] = newTopic
                    '''
                    End of Intiall the word was a general word
                    '''
                else:   
                    '''
                    Initial Specific Topic distribution c_t = 0
                    '''
                    #self.M[t][0] -= 1
                    #self.n_sk[curWordSeg][curTopic] -= 1
                    #self.nt_sk[curWordSeg][curTopic] -= 1
                    
                    # potential error not binomial
                    topicIndProb = ((self.M[t][0]+self.alpha_lambda[0])/
                                    (sum(self.M[t])+
                                     sum(self.alpha_lambda)))*((self.n_sk[curWordSeg][curTopic]+
                                                                self.nt_sk[curWordSeg][curTopic]+
                                                                self.alpha_theta)/(sum(self.n_sk[:,curTopic])+
                                                                                   sum(self.nt_sk[:,curTopic])+
                                                                                   (self.K*self.alpha_theta)))
                
                    newInd = np.random.binomial(1,1-topicIndProb)
                    
                    if newInd==1:
                        '''
                        The new distribution is general.
                        '''
                        self.M[t][1] += 1
                        # sample z_t
                        #self.n_sw[curTopic][word] -= 1
                        #self.n_tw[curTopic][word] -= 1   This has already been done
                        #self.n_ik[curTopic] -= 1   There is no need to decrement. it is a new assignment
                        
                        newTopicProb = ((self.n_sw[:,word]+self.n_tw[:,word]+self.beta)/
                                    (sum(self.n_sw[:,word])+sum(self.n_tw[:,word])+
                                     (self.beta*self.N)))*((self.n_ik+self.alpha_psi)/sum(self.n_ik)+
                                                           (self.K*self.alpha_psi))
                        
                        newTopic = np.random.multinomial(1, newTopicProb / newTopicProb.sum()).argmax()
                        
                        #self.n_sw[newTopic][word] += 1
                        self.n_tw[newTopic][word] += 1
                        self.n_ik[newTopic] += 1
                        
                        z_t[w] = newTopic
                        segInd[w] = -1      # general distribution hence -1 as segment indicator
                        
                    else:
                        '''
                        The new distribution is a again specific distribution. So we will have to choose a segment 
                        and then a topic
                        '''
                        self.M[t][0] += 1
                        
                        # sample s_t
                        #self.n_sk[curWordSeg][curTopic] -= 1
                        # self.nt_sk[curWordSeg][curTopic] -= 1   This has already been done
                        #self.n_is[t][curWordSeg][t] -= 1
                        
                        segProb = ((self.n_sk[:,curTopic]+ 
                                    self.nt_sk[:,curTopic]+
                                    self.alpha_theta)/(sum(self.n_sk[:,curTopic])+
                                                       sum(self.nt_sk[:,curTopic])+
                                                       (self.K*self.alpha_theta))) *((self.n_is[:,t]+
                                                                                      self.alpha_gamma)/(sum(self.n_is[:,t])+ 
                                                                                     (self.alpha_gamma * self.S)))
                        
                        newSeg = np.random.multinomial(1, segProb / segProb.sum()).argmax()
                        
                        self.n_is[newSeg][t] += 1
                        segInd[w] = newSeg
                        
                        # sample z_t
                        
                        #self.n_sw[curTopic][word] -= 1
                        #self.n_tw[curTopic][word] -= 1
                        #self.n_sk[curWordSeg][curTopic] -= 1
                        #self.nt_sk[curWordSeg][curTopic] -= 1
                
                        newTopicProb = ((self.n_sw[:,word]+self.n_tw[:,word]+self.beta)/
                               (sum(self.n_sw[:,word])+sum(self.n_tw[:,word])+
                                (self.beta*self.N)))*((self.n_sk[newSeg]+ self.nt_sk[newSeg] + 
                                                       self.alpha_theta)/(sum(self.n_sk[newSeg])+
                                                                          sum(self.nt_sk[newSeg])+(self.K*self.alpha_theta)))
                        
                        newTopic = np.random.multinomial(1, newTopicProb / newTopicProb.sum()).argmax()
                        
                        #self.n_sw[newTopic][word] += 1
                        self.n_tw[newTopic][word] += 1
                        #self.n_sk[newSeg][newTopic] += 1
                        self.nt_sk[newSeg][newTopic] += 1
                        z_t[w] = newTopic
                        
                self.z_tn[t] = z_t
                self.segChoiceInd[t] = segInd        
        return
    
    def saveParameters(self):
        Theta = np.zeros((self.S,self.K))
        Phi = np.zeros((self.K,self.N))
        general = np.zeros((1,self.K)) 
        segStats = np.zeros((self.S,1))
        regionStats = np.zeros((2,1))
        
        for seg in range(self.S):
            Theta[seg] = ((self.n_sk[seg] + self.nt_sk[seg] + 
                           self.alpha_theta )/ (sum(self.n_sk[seg]) + sum(self.nt_sk[seg]) + (self.alpha_theta*self.K)))
        
        general = (self.n_ik + self.alpha_gamma ) / (sum(self.n_ik + (self.alpha_gamma*self.K)))
        
        Phi = np.zeros((self.K,self.N))
        for w in range(self.N):
            Phi[:,w] = ((self.n_sw[:,w] + self.n_tw[:,w] + 
                           self.beta )/ (sum(self.n_sw[:,w]) + sum(self.n_tw[:,w]) + (self.beta*self.N)))
        
        for t in range(self.T):
            segStats[self.n_is[:,t].argmax()] += 1
            regionStats[self.M[t].argmax()] += 1
            
        np.savetxt('E:/Dev/Python/Workspace/EtLDA/output/et-Topic-Word-Distribution.txt', Phi, delimiter='\t', fmt='%f')
        np.savetxt('E:/Dev/Python/Workspace/EtLDA/output/et-Seg-Topic-Distribution.txt', Theta, delimiter='\t', fmt='%f')
        np.savetxt('E:/Dev/Python/Workspace/EtLDA/output/et-general.txt', general, delimiter='\t', fmt='%f')
        np.savetxt('E:/Dev/Python/Workspace/EtLDA/output/et-segs.txt', segStats, delimiter='\t', fmt='%f')
        np.savetxt('E:/Dev/Python/Workspace/EtLDA/output/et-segs.txt', regionStats, delimiter='\t', fmt='%f')
        print "Saved all paramters"
        return
    
    def printTopics(self, numberOfWords):
        phi = np.genfromtxt(open('E:/Dev/Python/Workspace/LDA/output/et-Topic-Word-Distribution.txt','r'), delimiter='\t', dtype='f8')
        output = ""
        for i,topic in enumerate(phi):
            output = output + "Topic %s : "%i
            wordIndex = sorted(range(len(topic)), key=lambda k: topic[k], reverse=True)[:numberOfWords]
            for i in wordIndex:
                output = output + self.vocab[i] + ", "
            output = output + "\n"   
        
        file = open('E:/Dev/Python/Workspace/EtLDA/output/et-Topics.txt','w')
        file.write(output)
        print "Printed the topics"

if __name__=='__main__':
    myEtLda = EtLda(alpha_delta=0.1, alpha_gamma=0.1, alpha_lambda=[0.2,0.8], alpha_theta=0.1, alpha_psi=0.1, beta=0.01, KTopics=10)
    for i in range(200):
        if i%10==0:
            print "iteration %f" %i
        try:
            myEtLda.gibbsSampling()
        except:
            myEtLda.saveParameters()
            myEtLda.printTopics(30)
    
    myEtLda.saveParameters()
    myEtLda.printTopics(20)