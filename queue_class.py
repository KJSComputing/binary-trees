class Queue:

    MAXSIZE = 10

    #Constructor
    def __init__(self):

      # initializing queue with none
      self.maxsize = 100
      self.q = [None for i in range(self.maxsize)]
      self.start = 0
      self.end = -1
      self.size = 0


    def enqueue(self, data):

      if self.isFull():
        print("Queue is Full")

      else:

        if self.end == self.maxsize - 1:
          self.end = 0
        else:
          self.end = self.end + 1
        self.q[self.end] = data
        self.size = self.size + 1


    def isFull(self):
        if self.size == self.maxsize:
            return True
        else:
            return False


    def dequeue(self):
      if self.isEmpty():
        print ("Queue is empty")
        self.start = 0
        self.end = -1

      else:
        data = self.q[self.start]

        if self.start == self.maxsize:
          self.start = 0
        else:
          self.start = self.start + 1
          self.size = self.size - 1
        return data

    def isEmpty (self):
      if self.size == 0:
        return True
      else:
        return False

    def peek(self):
        return self.q[self.start]

    def displayQueue(self):

      if self.isEmpty():
          print("Queue is empty")
      else:

        for i in range (self.size):

          temp_start = self.start
          if i < self.maxsize -1:
            print(self.q[temp_start + i])
          else:
            temp_start = 0
            print(self.q[temp_start])

    def getSize(self):
      return self.size

    def reset(self):

      self.end = -1
      self.start = 0
      self.size = 0