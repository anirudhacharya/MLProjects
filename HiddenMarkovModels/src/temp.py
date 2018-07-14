
# Hidden Markov Model -- Brown Corpus
# Andrew Beinstein
import re
import string
import random

class HiddenMarkov:
  # Creates a Hidden Markov Model, given S, K, A, B, and PI
  # NOTE: K and columns of B should be in same order
  def __init__(self, S, K, A, B, pi):
    self.S = S
    self.K = K
    self.A = A
    self.B = B
    self.pi = pi
    self.numStates = len(S)
    self.numObs = len(K)
    self.observation_hash = self.construct_observation_hash()
    
  # Creates a hash to be used in converting a string into a list of numbers
  def construct_observation_hash(self):
    key = {}
    for index, letter in enumerate(self.K):
      key[letter] = index
    return key
  
  # Checks if a word is in its converted (i.e. integer) form
  def word_is_converted(self, word):
    return isinstance(word[0], int)
    
  # Converts a string of characters (in self.K) to a list of integers,
  # using the self.observation_hash
  def convert_obs(self, Obs):
    if not self.word_is_converted(Obs):
      encoded_obs = [0 for x in Obs]
      for i in range(len(Obs)):
        encoded_obs[i] = self.observation_hash[Obs[i]]
      return encoded_obs
    else:
      return Obs
  
  # Computes the forward-algorithm, or alpha-pass, given an observation O
  # Alpha is an N X T+1 matrix, where N is the number of states, and T is the length of observation
  def forward_algorithm(self, O):
    #O = self.convert_obs(O)
    for t in range(len(O)+1):
      if t == 0:
        alpha = [[0. for x in range(len(O) + 1)] for x in range(self.numStates)]
        for i in range(self.numStates):
          alpha[i][0] = self.pi[i] # Initial probability of being in state i

      else:
        for j in range(self.numStates): # Iterate through each row in Alpha
          for i in range(self.numStates): # Iterate through all the states in previous column
            alpha[j][t] += alpha[i][t-1] * self.A[i][j] * self.B[i][O[t-1]]
    return alpha
   
  # Returns the final forward probability
  def get_alpha_prob(self, alpha):
    prob = 0
    lenObs = len(alpha[0])
    for i in range(self.numStates):
      prob += alpha[i][lenObs - 1]
    return prob
    
  # Computes the backward-algorithm, or beta-pass, given an observation O
  # Beta is an N X T+1 matrix, where N is the number of states, and T is the length of observation
  def backward_algorithm(self, O):
    #O = self.convert_obs(O)
    for t in reversed(range(len(O) + 1)):
      if t == len(O):
        beta = [[0. for x in range(len(O) + 1)] for x in range(self.numStates)]
        for i in range(self.numStates):
          beta[i][t] = 1
      elif t == len(O) - 1:
        for i in range(self.numStates):
          beta[i][t] = self.B[i][O[t]]
      elif t >= 0:
        for i in range(self.numStates):
          for j in range(self.numStates):
            beta[i][t] += self.A[i][j] * self.B[i][O[t]] * beta[j][t+1]
    return beta
  
  # Returns the final backward probabiilty
  def get_beta_prob(self, beta):
    prob = 0
    for i in range(self.numStates):
      prob += beta[i][0] * self.pi[i]
    return prob
  
  # Probability of traversing an arc from state i to state j at time t
  # 1 <= t <= T      
  def arc_traverse_prob(self, i, j ,t, alpha, beta, O):
    t = t-1 # Indexing (why do Manning and Schutze insist on 1-based indexing!?!?)
    numer = alpha[i][t] * self.A[i][j] * self.B[i][O[t]] * beta[j][t+1]
    denom = 0 
    for m in range(self.numStates):
      for n in range(self.numStates):
        denom += alpha[m][t] * self.A[m][n] * self.B[m][O[t]] * beta[n][t+1]
    # print "numer: %f, denom: %f" % (numer,denom)
    # if denom == 0:
    #   denom = 0.001
    
    return numer / denom
    
  # Returns the soft counts of letters in a particular corpus 
  # A corpus is a list of words with elements from self.K   
  def soft_counts(self, corpus):
    # This is a hash of the following form:
    # {"letter": {state_1: count_emits_state_1, state_2: count_emits_state_2}}
    emission_counts = {}
    
    for letter in self.K:
      emission_counts[letter] = {}
      for state in self.S:
        emission_counts[letter][state] = 0

    for word in corpus:
      word = self.convert_obs(word)
      alpha = self.forward_algorithm(word)
      beta = self.backward_algorithm(word)
      for index, letter in enumerate(list(word)):
        letter_rep = self.K[int(letter)]
        for i in range(self.numStates):
          for j in range(self.numStates):
            # print "i: %i, j: %i, index: %i" % (i, j, index)
            # print "alpha: " + str(alpha) + ", beta: " + str(beta)
            # print "word: " + str(word)
            emission_counts[letter_rep][self.S[i]] += self.arc_traverse_prob(i, j, index, alpha, beta, word)
            
    return emission_counts
    
    
  # Generates the gamma values, referenced in Manning and Schutze
  # This returns an N x T matrix, where N is the number of states, and 
  # T is the number of letters in the word.  
  def generate_gamma(self, word):
    word = self.convert_obs(word)
    alpha = self.forward_algorithm(word)
    beta = self.backward_algorithm(word)
    gamma = [[0. for t in range(len(word))] for i in range(self.numStates)]
    for i in range(self.numStates):
      for t in range(len(word)):
        for j in range(self.numStates):
          gamma[i][t] += self.arc_traverse_prob(i, j, t+1, alpha, beta, word)
          
    return gamma
      
    
  # This takes a corpus and chooses the correct initial distribution,
  # based on gamma.
  def maximize_pi(self, corpus):
    current_pi = self.pi
    total_state_counts = [0 for i in range(self.numStates)]
    for word in corpus:
      gamma = self.generate_gamma(word)
      for i in range(len(total_state_counts)):
        total_state_counts[i] += gamma[i][0]
    total = sum(total_state_counts)
    
    new_pi = total_state_counts
    for i in range(len(total_state_counts)):
      new_pi[i] /= total
    return new_pi
    
  # This takes a corpus and chooses the correct transition matrix (A)
  def maximize_transitions(self, corpus):
    new_A = [[0. for i in range(self.numStates)] for i in range(self.numStates)]
    
    for word in corpus:
      word = self.convert_obs(word)
      alpha = self.forward_algorithm(word)
      beta = self.backward_algorithm(word)
      gamma = self.generate_gamma(word)
      
      for i in range(self.numStates):
        for j in range(self.numStates):
          numerator = 0 # Expected number of transitions from state i to j
          denom = 0 # Expected number of transitions from state i
          for t in range(len(word)):
            numerator += self.arc_traverse_prob(i, j, t+1, alpha, beta, word)
            denom += gamma[i][t]

          # if numerator == 0.:
          #   new_A[i][j] = 0.
          # else:
          #   new_A[i][j] += numerator / denom
          new_A[i][j] += numerator / denom

      # Normalize
    for i in range(self.numStates):
      total = 0
      for j in range(self.numStates):
        total += new_A[i][j]
      for j in range(self.numStates):
        new_A[i][j] /= total   
    

    return new_A
          
  def maximize_emissions(self, corpus):
    new_B = [[0. for i in range(len(self.K))] for j in range(self.numStates)]
    
    for word in corpus:
      word = self.convert_obs(word)
      alpha = self.forward_algorithm(word)
      beta = self.backward_algorithm(word)
      gamma = self.generate_gamma(word)
      
      for i in range(self.numStates):
        for t in range(len(self.K)):
          numerator = 0 # Expected # of transitions from state i with word[t] observed
          denom = 0 # Expected # of transitions from state i
          letter = self.K[t]
          for index in range(len(word)):
            if word[index] == self.observation_hash[letter]:
              numerator += gamma[i][index]
            denom += gamma[i][index]
          # if numerator == 0.:
          #   new_B[i][t] = 0.
          # else:
          #   new_B[i][t] = numerator / denom
          new_B[i][t] += numerator / denom
          

    # Normalize
    for i in range(len(new_B)):
      row_total = sum(new_B[i])
      for j in range(len(new_B[i])):
        new_B[i][j] /= row_total
          
    return new_B
    
  # This prints the soft counts (2 states) in a tabular form
  def print_soft_counts_two_state(self, corpus):
    soft_counts = self.soft_counts(corpus)
    print "letter" + "\t\t" + "S1" + "\t\t" + "S2" + "\t" + "S1/S2"
    for letter in soft_counts.keys(): 
      s1_count = soft_counts[letter]['S1']
      s2_count = soft_counts[letter]['S2']
      if s2_count == 0:
        s2_count = 0.0001
      ratio = s1_count / s2_count
      print "%s \t %f \t %f \t %f" % (letter, s1_count, s2_count, ratio)
      
  # This prints the soft counts (3 states) in a tabular form
  def print_soft_counts_three_state(self, corpus):
    soft_counts = self.soft_counts(corpus)
    print "letter" + "\t\t" + "S1" + "\t\t" + "S2" + "\t" + "S3"
    for letter in soft_counts.keys(): 
      s1_count = soft_counts[letter]['S1']
      s2_count = soft_counts[letter]['S2']
      s3_count = soft_counts[letter]['S3']
     # print "%s \t %f \t %f \t %f" % (letter, s1_count, s2_count, s3_count) 
    
 
    
# This runs the 2-state Hidden Markov Model on the Brown Corpus, given the number of words from Brown Corpus
def run_two_state(numWords):
  (A, B, pi) = build_random_uniform_data(2, 27)
  hmm = build_brown_corpus_data_two_state((A, B, pi))
  corpus = get_brown_corpus_wordlist(numWords)     
  
  # Run 10 times
  maxIters = 10
  for i in range(maxIters):
    A = hmm.maximize_transitions(corpus)
    B = hmm.maximize_emissions(corpus)
    pi = hmm.maximize_pi(corpus)
    print '-------' + str(i) + "/" + str(maxIters) + '--------'
    model = (A,B,pi)
    hmm = build_brown_corpus_data_two_state(model)
  
  hmm.print_soft_counts_two_state(corpus) 
 
# This runs the 3-state Hidden Markov Model on the Brown Corpus, given the number of words from Brown Corpus 
def run_three_state(numWords):
  hmm = build_brown_corpus_data_three_state()
  corpus = get_brown_corpus_wordlist(numWords)     
  
  # Run 10 times
  for i in range(10):
    A = hmm.maximize_transitions(corpus)
    B = hmm.maximize_emissions(corpus)
    pi = hmm.maximize_pi(corpus)
    print '-------' + str(i) + '--------'
    model = (A,B,pi)
    hmm = build_brown_corpus_data_three_state(model)
  
  hmm.print_soft_counts_three_state(corpus)

# ------------- HELPER METHODS ------------------ #

   
# Returns the tuple (A, B, PI) with randomized probability distributions 
def build_random_data(N, M):
  # Build A
  A = [[0. for i in range(N)] for i in range(N)]
  for i in range(N):
    sum = 0
    for j in range(N):
      p = random.random()
      A[i][j] = p
      sum += p
    for j in range(N):
      A[i][j] /= sum
      
  # Build B
  B = [[0. for i in range(M)] for i in range(N)]
  for i in range(N):
    sum = 0
    for j in range(M):
      p = random.random()
      B[i][j] = p
      sum += p
    for j in range(M):
      B[i][j] /= sum
  
  # Build PI    
  PI = [0. for i in range(N)]
  sum = 0
  for i in range(N):
    p = random.random()
    PI[i] = p
    sum += p
    
  for i in range(N):
    PI[i] /= sum
  return (A, B, PI)
  
# This provides randomized parameters (A, B, pi), but makes sure they're relatively uniform.
def build_random_uniform_data(N,M):
  # Build A
  frac = 1./N
  A = [[frac for i in range(N)] for i in range(N)]
  for i in range(N):
    sum = 0
    for j in range(N):
      interval = frac / 3
      offset = random.uniform(interval*-1,interval)
      A[i][j] += offset
      sum += A[i][j]
    for j in range(N):
      A[i][j] /= sum
      
  # Build B
  frac = 1./M
  B = [[frac for i in range(M)] for i in range(N)]
  for i in range(N):
    sum = 0
    for j in range(M):
      interval = frac / 3
      offset = random.uniform(interval*-1,interval)
      B[i][j] += offset
      sum += B[i][j]
    for j in range(M):
      B[i][j] /= sum
      
  # Build Pi
  frac = 1./N
  pi = [frac for i in range(N)]
  sum = 0
  for i in range(N):
    interval = frac / 3
    offset = random.uniform(interval*-1, interval) 
    pi[i] += offset
    sum += pi[i]
    
  for i in range(N):
    pi[i] /= sum
    
  return (A, B, pi)
  
# HMM for Brown Corpus with two states
# For now, this uses a randomized probability distribution
def build_brown_corpus_data_two_state((A, B, pi)=build_random_uniform_data(2,27)):
  S = ["S1", "S2"]
  K = list("#abcdefghijklmnopqrstuvwxyz")
  return HiddenMarkov(S, K, A, B, pi)

# HMM for Brown Corpus with three states
# For now, this uses a randomized probability distribution
def build_brown_corpus_data_three_state((A, B, pi)=build_random_uniform_data(3,27)):
  S = ["S1", "S2", "S3"]
  K = list("#abcdefghijklmnopqrstuvwxyz")
  return HiddenMarkov(S, K, A, B, pi)

    
# Gets the first MAX_WORDS words from the Brown Corpus
# in a format readable by the HMM. So, all word boundries are marked
# with a '#' character, and all puntuation is removed.
def get_brown_corpus_wordlist(MAX_WORDS):
  corpus = open("Browncorpus.txt", 'r')
  word_list = []

  counter = 0
  for line in corpus:
    line = re.sub(r'[^\w\s]', '', line)
    words = re.findall(r"([a-zA-Z]+)[ .,!?;\n\r]+", line.lower())
    for w in words:
      w = "#" + w + "#"
      word_list.append(w)
      counter += 1
      if counter == MAX_WORDS:
        break
    if counter == MAX_WORDS:
      break
  return word_list

# This is the main function that generates the soft counts from the brown corpus
def generate_soft_counts_brown_corpus():
  hmm = build_brown_corpus_data()
  word_list = get_brown_corpus_wordlist(1000)
  soft_counts = hmm.soft_counts(word_list)
  print "letter" + "\t\t" + "S1" + "\t\t" + "S2" + "\t" + "S1/S2"
  for letter in soft_counts.keys(): 
    s1_count = soft_counts[letter]['S1']
    s2_count = soft_counts[letter]['S2']
    ratio = s1_count / s2_count
    print "%s \t %f \t %f \t %f" % (letter, s1_count, s2_count, ratio)
  print soft_counts

# -------------- TESTING METHODS ----------------- #

# HMM Test Data (used for debugging)  
def build_test_data():
  S = ["S1", "S2"]
  K = ["b", "d", "a", "i", "k", "e"]
  #A = [[.25, .75], [.75, .25]]
  #B = [[.13, .14, .15, .16, .2, .22], [.22, .2, .16, .15, .14, .13]]
  #pi = [.75, .25]
  (A, B, pi) = build_random_uniform_data(2,6)
  pi = [.25, .75]
  return HiddenMarkov(S, K, A, B, pi)

def build_test_data2(A, B, pi):
  S = ["S1", "S2"]
  K = ["b", "d", "a", "i" ,"k", "e"]
  return HiddenMarkov(S, K, A, B, pi)
  
# Runs Test Data
def run_test():
  hmm = build_test_data()
  corpus = ["babekida", "dakekiba", "bebadidaki"]

  for i in range(10):
    new_A = hmm.maximize_transitions(corpus)
    new_B = hmm.maximize_emissions(corpus)
    new_pi = hmm.maximize_pi(corpus)
    hmm = build_test_data2(new_A, new_B, new_pi)
  soft_counts = hmm.soft_counts(corpus)
  for letter in soft_counts.keys():
    s1_count = soft_counts[letter]['S1']
    s2_count = soft_counts[letter]['S2']
    ratio = s1_count / s2_count
    print "%s \t %f \t %f \t %f" % (letter, s1_count, s2_count, ratio)
  
def run_book_test():
  hmm = build_book_data()
  corpus = ["lic"]
  O = hmm.convert_obs(list(corpus[0]))
  alpha = hmm.forward_algorithm(O)
  beta = hmm.backward_algorithm(O)
  print "alpha: " + str(hmm.get_alpha_prob(alpha))
  print "beta: " + str(hmm.get_beta_prob(beta))
  gamma = hmm.generate_gamma(corpus[0])
  print "gamma:" + str(gamma)

  new_A = hmm.maximize_transitions(corpus)
  new_B = hmm.maximize_emissions(corpus)
  new_pi = hmm.maximize_pi(corpus)
  print "Reestimated A: " + str(new_A)
  print "Reestimated B: " + str(new_B)
  print "Reestimated pi: " + str(new_pi)
  soft_counts = hmm.soft_counts(corpus)
  print soft_counts
  
# HMM Test Data (used for debugging)
def build_book_data():
  S = ["CP", "IP"]
  K = ["c", "i", "l"]
  A = [[.7, .3], [.5, .5]]
  B = [[.6, .1, .3], [.1, .7, .2]]
  pi = [1, 0]
  return HiddenMarkov(S, K, A, B, pi)
  
def gamma_tester():
  hmm = build_brown_corpus_data()
  word_list = get_brown_corpus_wordlist(10)
  pi = hmm.maximize_parameters(word_list)
  print pi
  
def transition_tester():
  hmm = build_brown_corpus_data()
  word_list = get_brown_corpus_wordlist(10)
  transitions = hmm.maximize_transitions(word_list)
  print transitions
  
def emissions_tester():
  hmm = build_brown_corpus_data()
  word_list = get_brown_corpus_wordlist(1000)
  emissions = hmm.maximize_emissions(word_list)
  print emissions
    

run_two_state(1000)
#run_three_state(1000)
#run_test()
#run_book_test()

