#Chapter 5.2


#5.2.1, 5.2.2, 5.2.3  See diagrams PDF.

#5.2.4 See diagrams PDF.


class Node:
    def __init__(self, R):
        self.val = None
        self.next = [None] * R

class Tries:
    def __init__(self, R):

        self.R = R
        self.root = Node(self.R)

    def get(self, key):

        index = 0
        node = self.root
        while(True):
            character = key[index:index+1]
            ascii_value = ord(character)
            if node.next[ascii_value] == None:
                return None
            else:
                if index == len(key)-1:
                    return node.next[ascii_value].val
                else:
                    node = node.next[ascii_value]
            index +=1

    def put(self, key, val):
        index = 0
        node = self.root
        while (True):
            character = key[index:index + 1]
            ascii_value = ord(character)

            if node.next[ascii_value] == None:
                node.next[ascii_value] = Node(self.R)
                node = node.next[ascii_value]
            else:
                node = node.next[ascii_value]

            if index == len(key) - 1:
                node.val = val
                return val
            index += 1


# trie = Tries(256)
# #
# # trie.put("snowboard", 22)
# # trie.put("ski", 11)
# # trie.put("slush", 33)
# # trie.put("powder", 44)
# #
# # print(trie.get("snowboard"))
# # print(trie.get("sky"))
# # print(trie.get("powder"))

class TSTNode:
    def __init__(self, c):
        self.c = c
        self.left = None
        self.mid = None
        self.right = None
        self.val = None

class TernarySearchTrie:
    def __init__(self):
        self.root = None

    def get(self, key):

        node = self.root
        index = 0

        while(True):

            if node == None:
                return None

            if index == len(key)-1:
                return node.val

            character = key[index:index + 1]

            ascii_value = ord(character)

            if ascii_value < node.c:
                node = node.left
            elif ascii_value > node.c:
                    node = node.right
            elif index < len(key) - 1:
                node = node.mid

            index +=1

    def put(self, key, val):

        node = self.root
        index = 0

        while (True):

            if index == len(key)-1:
                node.val = val
                return

            character = key[index:index + 1]
            ascii_value = ord(character)

            if self.root == None:
                self.root = TSTNode(ascii_value)
                index +=1
                node = self.root
                continue

            if ascii_value < node.c:
                if node.left == None:
                    node.left = TSTNode(ascii_value)
                node = node.left
            elif ascii_value > node.c:
                if node.right == None:
                    node.right = TSTNode(ascii_value)
                node = node.right
            elif index < len(key) - 1:
                if node.mid == None:
                    node.mid = TSTNode(ascii_value)
                node = node.mid



            index += 1



# tst = TernarySearchTrie()
#
# tst.put("databases", 11)
# tst.put("algorithms", 22)
# tst.put("operating_systems", 33)
# tst.put("ai", 44)
#
# print(tst.get("ai"))
# print(tst.get("algorithms"))