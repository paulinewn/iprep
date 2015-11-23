Design a cache ------------------------------------
Make neural networks scalable across large datasets ----------
 1st interview question - How can you merge k sorted data   
 streams using O(1) RAM? Also, explain in detail how will 
 you define the data stream object and its related functions
 /operations. 2nd interview questions - 

 1. Write a code that 
 accepts integers as arrays and outputs the multiplication 
 result as an array. 2. 

 Write a code that takes the coordinates 
  multiple rectangles as input and returns as output the 
  coordinates of the rectangle that is the intersection of 
  all the rectangles. 
  Scale for a paragraph, to a file that doesn't fit in memory 
  to a large set of files split across a network that don't fit 
  in memory of a single machine.

  LRU Cache:  OrderedDict ------------------------------------
  class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
LRU Cache: Regular dict ---------------------------------------
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1
What ---
Enumerating all possible combination of dictionary words to that can be 
formed in a 4x4 grid of characters such that subsequent characters in the 
word is adjacent in the grid.  