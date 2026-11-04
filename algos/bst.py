"""
Implement a binary search tree

Binary Seach Tree:
- Made up of nodes that hold one key and two children at most
- For every node, everything in the subtree to its left is less smaller
  and everything to its right is larger

Supports
- Search: start at the root and compare -> if target is smaller traverse left, if the target is larger traverse right. Value is found when the target == node. 
- Insert: Follows the same path as search, once you reach an empty spot --> insert value 
- Deletion: Three cases
    1. A leaf, just delete it
    2. A leaf with one child --> child takes its place
    3. Two children --> replace with the smallest node in its right subtree,
- Min/Max: Traverse all the way left or right --> min/max

Implimentation
- Node class: Has a reference to its own value (key) and too its children.
    Has only a key parameter, and two children attributes (left & right)
    Children are set to None because when a new node is inserted it begins with no children
- Tree class: Is a wrapper around the nodes.
    Every new tree begins empty, hence it only has "self" parameter.
- Insert for tree class: Use recursion to traverse the tree, each call to _insert references the node its currently on and then moves left, right or inserts --> then calls _insert again, etc.

Recursion: Process of defining a problem or funciton in terms of smaller/simpler versions of itself.
"""


class Node:
    def __init__(self, key):
        self.key 
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)









