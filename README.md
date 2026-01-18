# Binary Trees, DFS, and BFS

## Overview
This project introduces **Binary Trees** and fundamental **tree traversal algorithms**, focusing on **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**. You are provided with a partially implemented Python binary tree and must complete several traversal and search methods.

The objective is to understand how tree structures work and how different traversal strategies visit nodes in different orders.

---

## What Is a Binary Tree?
A **binary tree** is a hierarchical data structure where:
- Each node stores a value
- Each node has at most **two children**
  - a **left child**
  - a **right child**

### Key Terms
- **Root** – the top node of the tree
- **Parent** – a node with children
- **Child** – a node connected below a parent
- **Leaf** – a node with no children
- **Subtree** – a tree formed from a node and its descendants

Binary trees are widely used in searching, sorting, and representing hierarchical data.

---

## Tree Traversal
Tree traversal means **visiting every node exactly once** in a defined order.

There are two main traversal strategies:
- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**

---

## Depth-First Search (DFS)
DFS explores as far down a branch as possible before backtracking.

### Common DFS Traversals

#### Inorder Traversal (Left → Root → Right)
- Visit the left subtree
- Visit the current node
- Visit the right subtree

Used in Binary Search Trees to produce sorted output.

#### Postorder Traversal (Left → Right → Root)
- Visit the left subtree
- Visit the right subtree
- Visit the root node last

Useful for deleting trees and evaluating expression trees.

DFS is typically implemented using **recursion** or a **stack**.

---

## Breadth-First Search (BFS)
BFS traverses the tree **level by level**, starting from the root.

- Visits all nodes at depth 0
- Then depth 1, depth 2, and so on

BFS uses a **queue** and is also called **level-order traversal**.

---

## Example Binary Tree and Traversal Outputs (Using the Provided Example)

Here is the example binary tree (a Binary Search Tree):

```
          50
         /  \
        30  70
       / \  / \     
      20 40 60 80
```

### Preorder Traversal (Root → Left → Right)
**Output:**
```
50, 30, 20, 40, 70, 60, 80
```

### Inorder Traversal (Left → Root → Right)
**Output:**
```
20, 30, 40, 50, 60, 70, 80
```

### Postorder Traversal (Left → Right → Root)
**Output:**
```
20, 40, 30, 60, 80, 70, 50
```

### Breadth-First Search (BFS / Level-Order Traversal)
**Output:**
```
50, 30, 70, 20, 40, 60, 80
```

---

## Project Task Instructions

### Files Provided
- `main.py`

### Task
Complete the code for the following subroutines:

1. **`inorder()`**
   - Perform an inorder traversal
   - Follow: Left → Root → Right

2. **`postorder()`**
   - Perform a postorder traversal
   - Follow: Left → Right → Root

3. **`searchforitem(item)`**
   - Search the tree for a given value
   - Return `True` if found, otherwise `False`

---

## Guidelines
- Ensure clean formatting and readable code
- Test your code with multiple tree structures

---

## Learning Outcomes
By completing this task, you will be able to:
- Explain binary tree structure
- Differentiate DFS and BFS
- Implement traversals
- Search for values in a binary tree

---

Happy coding!
