import math
import sys

k_initialRadius = 1
k_radiusMultiplier = 2

#This implementation of QuadTree taken from www.pygame.org/wiki/QuadTree
#and modified to 
# - hold points instead of rectangles
# - find points within a given distance of an input point
class QuadTree(object):
    '''An implementation of a quad-tree.
    This implementation inserts items at the current level if they overlap all
    4 sub-quadrants, otherwise it inserts them recursively into the one or two
    sub-quadrants that they overlap.

    Items being stored in the tree must possess the following attributes:

    x - x coordinate
    y - y coordinate

    ...and they must be hashable.
  
    '''
    def __init__(self, items, depth=8, bounding_rect=None):
        """Creates a quad-tree.

        @param items:
        A sequence of items to store in the quad-tree. Note that these
        items must possess x and y attributes.
        
        @param depth:
        The maximum recursion depth.
        
        @param bounding_rect:
        The bounding rectangle of all of the items in the quad-tree. For
        internal use only.
        """
        # The sub-quadrants are empty to start with.
        self.nw = self.ne = self.se = self.sw = None
        
        # If we've reached the maximum depth then insert all items into this
        # quadrant.
        depth -= 1
        '''
        if depth == 0:
            self.items = items
            return
        '''
        # Find this quadrant's centre.
        if bounding_rect:
            l, t, r, b = bounding_rect
        else:
        # If there isn't a bounding rect, then calculate it from the items.
            l = min(item.x for item in items)
            t = min(item.y for item in items)
            r = max(item.x for item in items)
            b = max(item.y for item in items)
        cx = self.cx = (l + r) * 0.5
        cy = self.cy = (t + b) * 0.5
    
        self.items = []
        nw_items = []
        ne_items = []
        se_items = []
        sw_items = []
    
    for item in items:
      # Which of the sub-quadrants does the item overlap?
      in_nw = item.x <= cx and item.y <= cy
      in_sw = item.x <= cx and item.y >= cy
      in_ne = item.x >= cx and item.y <= cy
      in_se = item.x >= cx and item.y >= cy
          
      # If it overlaps all 4 quadrants then insert it at the current
      # depth, otherwise append it to a list to be inserted under every
      # quadrant that it overlaps.
      if in_nw and in_ne and in_se and in_sw:
        self.items.append(item)
      else:
        if in_nw: nw_items.append(item)
        if in_ne: ne_items.append(item)
        if in_se: se_items.append(item)
        if in_sw: sw_items.append(item)
      
    # Create the sub-quadrants, recursively.
    if nw_items:
      self.nw = QuadTree(nw_items, depth, (l, t, cx, cy))
    if ne_items:
      self.ne = QuadTree(ne_items, depth, (cx, t, r, cy))
    if se_items:
      self.se = QuadTree(se_items, depth, (cx, cy, r, b))
    if sw_items:
      self.sw = QuadTree(sw_items, depth, (l, cy, cx, b))

    def getPointsInCircle(self, loc, radius):
        """Returns the items that lie within a circle with center at loc

        Return type is a dict mapping Topic objects to distances from loc. This method
        is used to avoid recalculating the rectangle object on each recursive call to 
        getPointsHelper.
    
        @param loc:
          tuple (x,y) gives location of bounding circle's center

        @param radius:
          radius of bounding circle
        """
        rect = Rect(loc, radius)
        return self.getPointsHelper(loc, radius, rect)

    def getPointsHelper(self, loc, radius, rect):
        """Helper for getPointsInCircle. 
        Recursively finds the points that lie within a square that circumscribes the circle
        with center at loc and the given radius. Then filters out the points that are not
        within the circle.
    
        @param loc:
          tuple (x,y) gives location of bounding circle's center
    
        @param radius:
          radius of bounding circle
    
        @param rect:
          rectangle that circumscribes bounding circle
        """
        tDist = {}
        for item in self.items:
          d = getDistance((item.x, item.y), loc)
          if d <= radius:
            tDist[item] = d
        
        # Recursively check the lower quadrants.
        if self.nw and rect.left <= self.cx and rect.top <= self.cy:
          tDist.update(self.nw.getPointsHelper(loc, radius, rect))
        if self.sw and rect.left <= self.cx and rect.bottom >= self.cy:
          tDist.update(self.sw.getPointsHelper(loc, radius, rect))
        if self.ne and rect.right >= self.cx and rect.top <= self.cy:
          tDist.update(self.ne.getPointsHelper(loc, radius, rect))
        if self.se and rect.right >= self.cx and rect.bottom >= self.cy:
          tDist.update(self.se.getPointsHelper(loc, radius, rect))
    
        return tDist

class Topic(object):
  """Represents a topic with an integer ID and an (x,y) location."""
  def __init__(self, num, x, y):
    self.num = num
    self.x = x
    self.y = y
    self.questions = []

  def __repr__(self):
    return 'Topic %d, location (%f, %f), questions ' % (self.num, self.x, self.y) + str(self.questions)

  def addQuestion(self, questionNum):
    self.questions.append(questionNum)

class Rect(object):
  """The rectangle that QuadTree uses to bound its search for points."""
  def __init__(self, loc, radius):
    self.left = max(0,loc[0] - radius)
    self.right = loc[0] + radius
    self.top = max(0, loc[1] - radius)
    self.bottom = loc[1] + radius

def getDistance(loc1, loc2):
  return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

def doTopicQuery(numToGet, loc, topics):
  """Finds the topics closest to a given location.

  @param numToGet: 
    number of topics to find

  @param loc: 
    tuple (x,y) gives location to find topics near

  @param topics:
    a QuadTree containing all candidate topics

  Return type is a list containg numToGet topic numbers.
  """
  radius = k_initialRadius
  numTopics = min(topics.length, numToGet) 
  topicDistDict = {}
  while len(topicDistDict) < numTopics:
    topicDistDict = topics.getPointsInCircle(loc, radius)
    radius *= k_radiusMultiplier

  def cmpTopics(a, b):
    if abs(topicDistDict[a]-topicDistDict[b]) <= .001:
      return cmp(b.num, a.num)
    elif topicDistDict[a] > topicDistDict[b]:
      return 1
    else: # topicDistDict[a] < topicDistDict[b]
      return -1

  sortedTopics = sorted(topicDistDict.keys(), cmp=cmpTopics)
  topics = [sortedTopics[i].num for i in range(numTopics)]
  return topics

def doQuestionQuery(numToGet, loc, topics):
  """Finds questions near a given location.

  @param numToGet:
    number of questions to find

  @param loc:
    tuple (x,y) gives location to find questions near

  @param topics:
    a QuadTree containing all candidate topics

  Return type is a list containing numToGet question numbers.
  """
  qDist = {}
  radius = k_initialRadius 
  topicDistDict = {}
  while len(topicDistDict) < topics.length:
    questionSet = set()
    topicDistDict = topics.getPointsInCircle(loc, radius)
    for t,distance in topicDistDict.iteritems():
      for q in t.questions:
        qDist[q] = min(qDist.get(q, distance), distance)
      questionSet |= set(t.questions)
    if len(questionSet) >= numToGet:
      break
    radius *= k_radiusMultiplier
  def cmpQuestions(a, b):
    if abs(qDist[a]-qDist[b]) <= .001:
      return cmp(b,a)
    elif qDist[a] > qDist[b]:
      return 1
    else: #qDist[a] < qDist[b]
      return -1
  sortedQuestions = sorted(list(questionSet), cmp=cmpQuestions)
  return sortedQuestions[:numToGet]

def main():
  #parse the first line
  firstline = raw_input().split()
  numTopics = int(firstline[0])
  numQuestions = int(firstline[1])
  numQueries = int(firstline[2])

  #parse the topic lines
  topicsDict = {}
  for i in range(numTopics):
    topic = raw_input().split()
    topicNum = int(topic[0])
    topicsDict[topicNum] = Topic(topicNum, float(topic[1]), float(topic[2]))
  topics = QuadTree(topicsDict.values())
  topics.length = len(topicsDict)

  #parse the question lines
  for i in range(numQuestions):
    question = raw_input().split()
    questionNum = int(question[0])
    topicTags = question[2:]
    topicTags = [int(tt) for tt in topicTags]
    for topicNum in topicTags:
      topicsDict[topicNum].addQuestion(questionNum)

  #parse the query lines
  queryList = []
  for i in range(numQueries):
    queryList.append(raw_input().split())

  first = True
  for query in queryList:
    numToGet = int(query[1])
    loc = (float(query[2]), float(query[3]))
    #perform the query
    if query[0] is 't':
      ans = doTopicQuery(numToGet, loc, topics)
    elif query[0] is 'q':
      ans = doQuestionQuery(numToGet, loc, topics)

    #print output
    if not first:
      print
    first = False
    for a in ans:
      print '%d' %a,

if __name__ == '__main__':
  main()
