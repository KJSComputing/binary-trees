from queue_class import Queue
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

    def delete(self, item):
        # Hibbard deletion (successor = leftmost node of right subtree)

        current = self.root
        parent = None

        # 1) Find node to delete and its parent
        while current is not None and current.getData() != item:
            parent = current
            if item < current.getData():
                current = current.getLeft()
            else:
                current = current.getRight()

        # Not found
        if current is None:
            return False

        # Helper: replace parent's child pointer (or root) with new_child
        def replace_child(parent_node, old_child, new_child):
            if parent_node is None:
                self.root = new_child
            elif parent_node.getLeft() == old_child:
                parent_node.setLeft(new_child)
            else:
                parent_node.setRight(new_child)

        # 2) Case: no children (leaf)
        if current.getLeft() is None and current.getRight() is None:
            replace_child(parent, current, None)
            return True

        # 3) Case: one child (left only)
        if current.getRight() is None:
            replace_child(parent, current, current.getLeft())
            return True

        # 4) Case: one child (right only)
        if current.getLeft() is None:
            replace_child(parent, current, current.getRight())
            return True

        # 5) Case: two children
        # Find successor (leftmost in right subtree) and its parent
        succ_parent = current
        succ = current.getRight()
        while succ.getLeft() is not None:
            succ_parent = succ
            succ = succ.getLeft()

        # Copy successor's data into current node
        # If you have setData(), use: current.setData(succ.getData())
        current.data = succ.getData()

        # Remove successor node (successor has no left child)
        if succ_parent.getLeft() == succ:
            # successor may have a right child
            succ_parent.setLeft(succ.getRight())
        else:
            # successor was the direct right child of current
            succ_parent.setRight(succ.getRight())

        return True

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
        q = Queue()
        while current_node != None:
            print(current_node.getData())
            if current_node.getLeft() != None:
                q.enqueue(current_node.getLeft())
            if current_node.getRight() != None:
                q.enqueue(current_node.getRight())
            current_node = q.dequeue()

#Main program
tree = BinaryTree()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)

print("Preorder:")
tree.preorder(tree.root)

print("Inorder:")
tree.inorder(tree.root)

print("Postorder:")
tree.postorder(tree.root)

print("Search 10:", tree.searchforitem(tree.root, 10))
print("Search 99:", tree.searchforitem(tree.root, 99))
