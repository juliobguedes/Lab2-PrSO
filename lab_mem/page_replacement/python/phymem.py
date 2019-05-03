# This is the only file you must implement

# This file will be imported from the main code. The PhysicalMemory class
# will be instantiated with the algorithm received from the input. You may edit
# this file as you which

# NOTE: there may be methods you don't need to modify, you must decide what
# you need...

class PhysicalMemory(object):
  ALGORITHM_AGING_NBITS = 8
  """How many bits to use for the Aging algorithm"""

  def __init__(self, algorithm):
    assert algorithm in {"fifo", "nru", "aging", "second-chance"}
    self.algorithm = algorithm

  def put(self, frameId):
    """Allocates this frameId for some page"""
    # Notice that in the physical memory we don't care about the pageId, we only
    # care about the fact we were requested to allocate a certain frameId
    pass

  def evict(self):
    """Deallocates a frame from the physical memory and returns its frameId"""
    # You may assume the physical memory is FULL so we need space!
    # Your code must decide which frame to return, according to the algorithm
    pass

  def clock(self):
    """The amount of time we set for the clock has passed, so this is called"""
    # Clear the reference bits (and/or whatever else you think you must do...)
    pass

  def access(self, frameId, isWrite):
    """A frameId was accessed for read/write (if write, isWrite=True)"""
    pass

class FIFO(PhysicalMemory):
  def __init__(self):
    from Queue import Queue
    super(FIFO, self).__init__("fifo")

    self.queue = Queue()
  
  def put(self, frameId):
    self.queue.put(frameId)

  def evict(self):
    return self.queue.get()

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    pass

class NRU(PhysicalMemory):
  def __init__(self):
    super(NRU, self).__init__("nru")
  
  def put(self, frameId):
    pass

  def evict(self):
    return 0

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    pass

class Aging(PhysicalMemory):
  def __init__(self):
    super(Aging, self).__init__("aging")
  
  def put(self, frameId):
    pass

  def evict(self):
    return 0

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    pass

class SecondChance(PhysicalMemory):
  def __init__(self):
    super(SecondChance, self).__init__("second-chance")
  
  def put(self, frameId):
    pass

  def evict(self):
    return 0

  def clock(self):
    pass

  def access(self, frameId, isWrite):
    pass

