

#Chapther 3.3


#3.3.1

# answer = "1st          E" \
#  \
#          "2nd       A  E"\
#  \
#         "3rd           E" \
#     "                A   S"\
#  \
#         "4th           E"\
#                    " A   S Y"\
#   \
#         "5th           E S" \
#          "           A  Q  Y"\
#   \
#         "6th             E S "\
#         "              A  Q  UY" \
#   \
#         "7th                S" \
#          "                E  U" \
#          "              A  Q T  Y" \
#   \
#          "8th                S" \
#          "                E  U" \
#          "              A  IQ T  Y" \
#  \
#          "9th                S" \
#          "                EO    U" \
#          "              A I Q  T  Y" \
#  \


#3.3.4

answer =  "For a tree that is all three nodes, the structure resembles" \
          "   36"\
          "12 45 78" \
          "There are twice as many nodes than for a typical terary tree. Thus, the height is floor(log (3) n)." \
          "For a binary tree, the structure resembles" \
          "    2" \
          " 1    3" \
          "The height is floor(log(2) n). Thus, a tree that has a structure between these two extremes has a height between these" \
          "two calculations."


#3.3.5

answer = "7 nodes:" \
         "  NN" \
         "NN N NN" \
         "" \
         "  NN" \
         "N NN NN" \
         "" \
        "8 nodes:" \
         "   NN" \
         "NN NN NN" \
         "" \
         "9 nodes:"\
        "    N" \
         "  N   N" \
         "NN N N NN"\
        " "\
        "    N" \
         "  N   N" \
         "N  NN N NN"\
        ""\
        "    N" \
         "  N   N" \
         "N  NN NN N"\
        ""\
        "10 nodes:"\
        "    N" \
         "  N   N" \
         "NN  NN NN N"\
        ""\
        "    N" \
         "  N   N" \
         "N  NN NN NN"\
""\
        "    N" \
         "  N     NN" \
         "N  NN N  N N"\
""\
        "    N" \
         "  NN     N" \
         "N  N N  N NN"\


#3.3.9

answer = "3"


#3.3.11

answer = "See pdf."



#3.3.13

answer = "A monotonically increasing tree must never decrease in height. Since Red-black trees preserve balance, they are monotonically" \
         "increasing."

#3.3.15

answer = "Same answer as 3.3.13."


#3.3.17


class Node:
    def __init__(self, key, val, n, color):
        self.key = key
        self.value = val
        self.n = n
        self.color = color
        self.left = None
        self.right= None

class RedBlackBST:
    def __init__(self, root):
        self.root = root

    def isRed(self, node):
        if node[0] == None:
            return False
        return node[0].color == "Red"

    def rotateLeft(self, node):
        leftNode = node[0].right
        node[0].right = leftNode.left
        leftNode.left = node[0]
        leftNode.color = node[0].color
        node[0].color = "RED"
        leftNode.n = node[0].n
        node[0].n = 1 + self.size(node[0].left) + self.size(node[0].right)
        return leftNode

    def rotateRight(self, node):
        rightNode = node[0].left
        node[0].left = rightNode.right
        rightNode.right = node[0]
        rightNode.color = node[0].color
        node[0].color = "RED"
        rightNode.n = node[0].n
        node[0].n = 1 + self.size(node[0].left) + self.size(node[0].right)
        return rightNode

    def flipcolors(self, node):
        node[0].color = "RED"
        node[0].left.color = "BLACK"
        node[0].right.color = "BLACK"


    def size(self, node):
        if node == None:
            return 0
        else:
            return node.n

    def put(self, key, value):
        self.root = self.private_put(self.root, key, value)
        self.root.color = "BLACK"

    def private_put(self, node, key, value):

        if node == None:
            return Node(key, value, 1, "RED")

        if key < node.key:
            node.left = self.private_put(node.left, key, value)
        elif key > node.key:
            node.right = self.private_put(node.right, key, value)
        else:
            node.value = value

        if self.isRed((node.right,)) and self.isRed((node.left,)) != "RED":
            node = self.rotateLeft((node,))
        if self.isRed((node.right,)) and self.isRed((node.left.left,)):
            node = self.rotateRight((node,))
        if self.isRed((node.left,)) and self.isRed((node.right,)):
            node = self.flipcolors((node,))


        node.n = self.size(node.left) + self.size(node.right)

        return node

    def printer(self):

        self.printTree(self.root)

    def printTree(self, node):

        print("the key and value and color", node.key, node.value, node.color)

        if node.left != None:
            self.printTree(node.left)
        if node.right != None:
            self.printTree(node.right)





# root = Node(32, "Kyle", 1, "BLACK")
#
# redBlackBST = RedBlackBST(root)
#
# redBlackBST.put(35, "Rena")
# redBlackBST.put(29, "Nick")
# redBlackBST.put(25, "Alex")
# redBlackBST.put(40, "Summit")
# redBlackBST.printer()
# redBlackBST.put(39, "Rhadika")
# redBlackBST.put(41, "Summit older")
# redBlackBST.put(23, "Marko")
# redBlackBST.printer()
