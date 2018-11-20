#Chapter 5.3


#5.3.1

class BruteForce:

    def __init__(self, text):

        self.text = text;

    def search(self, pattern):

        pattern_length = len(pattern)
        text_length = len(self.text)

        for i in range(text_length-pattern_length):
            for j in range(pattern_length):
                if ord(self.text[i+j]) != ord(pattern[j]):
                    break;
            if j == pattern_length-1:
                return i

        return text_length


brute_search = BruteForce("Ilikeapplebytheloraxinthesky")

# print(brute_search.search("lorax"))


#5.3.2

DFA = {
    "A": [1, 2, 3, 4, 5, 6, 7, 8],
    "B": [0, 0, 0, 0, 0, 0, 0, 0],
    "C": [0, 0, 0, 0, 0, 0, 0, 0]

}


#5.3.3

pattern ="A  B  R  A  C  A  D  A  B  R  A"

DFA = {
    "A": [1, 1, 1, 4, 1, 6, 1, 8, 1, 1, 11],
    "B": [0, 2, 0, 0, 2, 0, 2, 0, 9, 0, 0],
    "C": [0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
    "D": [0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
    "R": [0, 0, 3, 0, 0, 0, 0, 0, 0, 10, 0]
}



#5.4.4

class BlankCounter:
    def __init__(self, text):
        self.count = 0;
        self.text = text

    def countBlanks(self, amount_of_blanks):

        for i in range(len(self.text)):

            if self.text[i] == " ":
                self.count += 1
            else:
                self.count = 0

            if self.count == amount_of_blanks:
                return i - amount_of_blanks


blanks = BlankCounter("Somewhere over the rain   bow, way up high")
# print(blanks.countBlanks(3))


#5.5.5

"""Assume a four letter alphabet: ABCD"""

right = [12, 13, 11, 9]


#5.5.6

"""Assume a five letter alphabet: ABCDR"""

right = [10, 8, 4, 6, 9]