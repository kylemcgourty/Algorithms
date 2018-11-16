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


trie = Tries(256)

trie.put("snowboard", 22)
trie.put("ski", 11)
trie.put("slush", 33)
trie.put("powder", 44)

print(trie.get("snowboard"))
print(trie.get("sky"))
print(trie.get("powder"))