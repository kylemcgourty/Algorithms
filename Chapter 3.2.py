

#3.2.1

BST = "E(6)" \
    "A(1)   S(7)" \
      "   Q(4)    Y(3)" \
      "I(9)  U(5)T(8)" \
      "  O(10)"\
       "N(11)"


#3.2.4

answer = "Sequence D cannot be the correct sequence"


#3.2.5

answer = 'The keys should not be inserted in order because that would lead to a worst-case shaped tree.' \
         'The best case runtimes for a BST occur where the tree is perfectly balanced.' \
         'This situation occurs when keys are inserted in a random order.'



#3.2.6


class BST:
    def __init__(self):
        self.start = 0;
        self.BST_height = 0
    class Node:
        def __init__(self, k, v, n):
            self.key = k
            self.value = v;
            self.n = n

    def size(self, node):
        return node.n

    def height(self, node):

        if node is None:
            return 0;

        ldepth = self.height(node.left)
        rdepth = self.height(node.right)

        if (ldepth > rdepth):
            return ldepth + 1
        else:
            return rdepth + 1


#3.2.8
from math import log, floor

class BST_1:

    def optCompare(self, n):
        """a perfectly balanced search tree has only Null links in its last (or last -1) row
        the number of compares it would take is thus lg n + 1, where +1 comes from the compare at the root"""
        return floor(log(n, 2));

#3.2.11

answer = "There are no binary trees of height n with n nodes. E.g. A height of 1 must have at least 2 nodes; a height" \
          "of 2 must have at least three nodes." \
          "To insert n distinct keys into a binary tree of height n-1 produces the Catalan number for n."


#3.2.13 and 3.2.14



class BST_2:
    def __init__(self):
        self.root = None
        self.BST_height = 0
    class Node:
        def __init__(self, k, v):
            self.key = k
            self.value = v
            self.left = None
            self.right = None

    def get(self, key):
        node = self.root
        while(True):
            if node == None:
                return None;
            if key < node.key:
                node = node.left
                continue
            if key > node.key:
                node = node.right
                continue
            if key == node.key:
                return node.value


    def put(self, key, value):
        if (self.root == None):
            self.root = self.Node(key, value)
            return
        else:
            node = self.root;

        while(True):
            if key < node.key:
                original = node
                node = node.left
                if node == None:
                    self.establish_node(original, "L", key, value)
                    break;
                continue
            if key > node.key:
                original = node
                node = node.right
                if node == None:
                    self.establish_node(original, "R", key, value)
                    break;
                continue
            if key == node.key:
                node.value = value
                break;

        return

    def establish_node(self, node, direction, key, value):
        if direction == "L":
            node.left = self.Node(key, value)
        if direction == "R":
            node.right = self.Node(key, value)

    def min(self):
        node = self.root

        while(True):
            if node.left != None:
                node = node.left
                continue
            else:
                return node.value

    def max(self):
        node = self.root

        while (True):
            if node.right != None:
                node = node.right
                continue
            else:
                return node.value

    def floor(self, key):
        node = self.root

        if key >= self.root.key and self.root.right == None:
            return self.root.key

        while(True):
            if node.key == key:
                return node.value
            if key < node.key:
                node = node.left
                if node == None:
                    return original_node.key
                continue
            if key > node.key:
                original_node = node
                node = node.right
                if node == None:
                    return original_node.key
                continue


# bst = BST_2()
#
#
# bst.put(11, "K")
# bst.put(5, "R")
# bst.put(22, "S")
# bst.put(33, "M")
# bst.put(17, "T")
#
#
# print("the floor val", bst.floor(12))