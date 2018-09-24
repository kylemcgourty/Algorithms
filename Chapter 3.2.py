

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
    def __init__(self):

    def optCompare(self, n):
        """a perfectly balanced search tree has only Null links in its last (or last -1) row
        the number of compares it would take is thus lg n + 1, where +1 comes from the compare at the root"""
        return floor(log(n, 2));

