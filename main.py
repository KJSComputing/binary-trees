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


class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

    def getLeft(self):
        return self.left

    def setLeft(self, new_node):
        self.left = new_node

    def getRight(self):
        return self.right

    def setRight(self, new_node):
        self.right = new_node

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, new_value):
        # Step 1: Create a New Node
        new_node = Node(new_value)

        # Step 2: Check if the Tree is Empty
        if self.root is None:
            self.root = new_node
            return

        # Step 3: Traverse the Tree to Find Insertion Point
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if new_value < current.getData():
                current = current.getLeft()
            else:
                current = current.getRight()

        # Step 4: Insert the Node
        if new_value < parent.getData():
            parent.setLeft(new_node)
        else:
            parent.setRight(new_node)

    def preorder(self,current_node):
        if current_node != None:
            #Visit each node: NLR
            print(current_node.getData())
            if current_node.getLeft != None:
                self.preorder(current_node.getLeft())
            if current_node.getRight() != None:
                self.preorder(current_node.getRight())

    def inorder(self,current_node):
            pass

    def postorder(self,current_node):
            pass

    def searchforitem(self, root, item):
        pass

    def bfs(self,current_node):
        q = queue()
        while current_node != None:
            print(current_node.getData())
            if current_node.getLeft() != None:
                q.enqueue(current_node.getLeft())
            if current_node.getRight() != None:
                q.enqueue(current_node.getRight())
            current_node = q.dequeue()

    def delete(self,item):
        #Using Hibbard's algorithm (leftmost node of right sub-tree is the successor)
        #Find the node to delete
        current_node = self.start
        while current_node != None and current_node.getData() != item:
            previous = current_node
            if item < current_node.getData():
                current_node = current_node.getLeft()
            else:
                current_node = current_node.getRight()

        #Handle 3 cases depending on the number of child nodes
        if current_node != None:
            if current_node.getLeft() == None and current_node.getRight() == None:
                #Node has no children
                if previous.data > current_node.getData():
                    previous.getLeft() = None
                else:
                    previous.getRight() = None
            elif current_node.getRight() == None:
                #Node has one left child
                if previous.getData() > current_node.getData():
                    previous.getLeft() = current_node.getLeft()
                else:
                    previous.getRight() = current_node.getLeft()
            elif current_node.getLeft() == None:
                #Node has one right child
                if previous.getData() < current_node.getData():
                    previous.getLeft() = current_node.getRight()
                else:
                    previous.getRight() = current_node.getRight()
            else:
                #Node has two children
                right_node = current_node.getRight()
                if right_node.getLeft() != None:
                    #Find the smallest value in the right sub-tree (successor node)
                    smallest = right_node
                    while smallest.getLeft() != None:
                        previous = smallest
                        smallest = smallest.getLeft()
                    #Change the deleted node value to the smallest value
                    current_node.data = smallest.getData()
                    #Remove the successor node
                    previous.getLeft() = None
                else:
                    #Handle special case of no left sub-tree from right node
                    current_node.data = right_node.getData()
                    current_node.getRight() = None

tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.preorder(tree.root)
tree.searchforitem(tree.root, 10)
