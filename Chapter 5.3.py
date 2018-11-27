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


# brute_search = BruteForce("Ilikeapplebytheloraxinthesky")

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



#5.3.4

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


# blanks = BlankCounter("Somewhere over the rain   bow, way up high")
# print(blanks.countBlanks(3))


#5.3.5

"""Assume a four letter alphabet: ABCD"""

right = [12, 13, 11, 9]


#5.3.6

"""Assume a five letter alphabet: ABCDR"""

right = [10, 8, 4, 6, 9]


#5.3.9

class BoyerMooreSubStringSearch:
    def __init__(self, pat):
        self.pat = pat
        self.m = len(self.pat)
        self.R = 256
        self.right = [-1]*self.R
        self.count = 0
        self.occurences = list()

        for i in range(self.m):
            self.right[ord(self.pat[i])] = i


    def search(self, text):

        self.n = len(text)

        i = 0
        while(i < self.n-self.m):
            skip = 0
            j = self.m-1
            while(j > 0):
                if(ord(self.pat[j]) != ord(text[i+j])):
                    skip = j - self.right[ord(text[i+j])]
                    if skip < 1:
                        skip = 1
                    break
                j -= 1
            if skip == 0:
                self.count +=1
                self.occurences.append(i)
                skip = self.m-1
                # return i
            i += skip


    def searchAll(self, text):

        self.search(text)

        for match in self.occurences:
            print("match at index", match, text[67:76])



# search = BoyerMooreSubStringSearch("reenbeans")

text = "The Lorax visited the Truffula trees and on the trees he found the reenbeans, a delicous fruit to delectable delight, so tangy and bright."
# search.searchAll(text)


#5.3.10

class RabinKarpSeach:
    def __init__(self, pattern):
        self.patHash = 0;
        self.pat = pattern
        self.m = len(self.pat)
        self.q = 127
        self.R = 256
        self.RM = 1
        for i in range(self.m-1):
            self.RM = (self.RM * self.R) % self.q

        self.patHash = self.hash(self.pat, self.m)

    def hash(self, text, m):
        h = 0
        for i in range(m):
            h = (self.R * h + ord(text[i])) % self.q
        return h

    def check(self, text, i):

        for char in self.pat:
            if char != text[i]:
                return False
            i +=1

        return True



    def search(self, text):

        self.n = len(text)
        textHash = self.hash(text, self.m)
        if self.patHash == textHash:
            return 0

        for i in range(self.n):

            textHash = (textHash + self.q - self.RM*ord(text[i]) % self.q)% self.q
            textHash = (textHash * self.R + ord(text[i+self.m])) % self.q

            if self.patHash == textHash:
                return self.check(text, i)

        return self.n



rabinKarp = RabinKarpSeach("reenbeans")

print("result", rabinKarp.search(text))


#5.3.11

answer = "A worst case scenario for the Boyer Moore algorithm would be a text of a repeating letter, which is the same " \
         "letter as the last letter of the pattern. Thus, every letter in the text would be examined."

#5.3.12  See 5.3.10


#5.3.13

answer = "When c is the penultimate (second last) occurence and it is also the last character of the sequence, then the right array may" \
         "be set to the penultimate occurence. This switch is possible because two back-to-back occurences of c exist in the pattern, which" \
         "voids the necessity of having to move the text twice by just one character."

#5.3.16

answer = """
A. The brute force pattern processes every sequence of AAAAAA until it reaches the end of the text where it compeletes its search
by processing AAAAAAAB.
B. The brute force algorithm processes various lengths of ABABABA until reaching the end of the text without a match.
"""

#5.3.18

answer = """
The length of the text that is searched is (n-m+1). The probability of not finding the correct characters in the random string
over the probability of finding other randoms characters, is the probability the pattern checking in loop will run, which is given
by (1-R ^-m)/(1-R^-1). Multiplied together, the run time will be less than 2(n-m+1).
"""

#5.3.19

answer = "When the last character of pattern is the only chaaracter in the text, Boyer-Moore would examine every character of the text."

