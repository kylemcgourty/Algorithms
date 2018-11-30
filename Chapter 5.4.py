#Chapter 5.4

#5.4.1

answer = """
RE for 4 consecutive A's: /(A){4}/
RE for not more than four consecutive A's: /(A){1-4}/
RE for at least one occurence of four consecutive A's: /((A){4})+/
"""

#5.4.2

answer = """
a. Any number of characters
b. A followed by any number of characters and then another A, or a single A
c. Any number of characters followed by ABBABBA, followed by another number of characters
d. The main sequence is any number of characters followed by A. This sequence is repated four times, followed by any number of characters.
"""

#5.4.3

answer = "The number of different strings than can be described is M + 1"


#5.4.4 See 5.4.4.pdf


#5.4.6

answer = """

Pattern ABBACEFGEFGCAAB

Transition states: 3 6 7 5 6 7 5 6 7 3 6 7 8 16 17 9 12 16 17 13 14 15 16 17 13 14 15 16 17 9 12 16 17 3 4 6 3 4 6 5 6 8 16 17 18 19 """


#5.4.7

import re

class Grep:
    def __init__(self, pattern):
        self.pattern = r"(" + pattern + ")"

    def grep(self, text):
        matches = re.findall(self.pattern, text)
        print("the result", matches)

tinyLtext = "AC AD AAA ABD ADD BCD ABCCBD BABAAA BABBAAA"


grep = Grep("(A|B)(C|D)")

grep.grep(tinyLtext)


#5.4.8

answer = """
a. /1{3,}/
b. /110/
c. /(110){2}0/
d. /(?!110)/
"""


#5.4.9

answer = "/(0(.+)0)+/"


#5.4.10


answer = """"

a. /(.{1})(.{1})0.*/
b. /(0{3})+/
c. /(.)+.*(\1)/
d. /.(..)*/
e. /(0(..)*)|((1(.))+(..)*)/
f. /.+(..)?/

"""


#5.4.11

answer = """

a. 2^(988)
b. 1000 * 333
c. TBC
"""


#5.4.12

answer = """

a. /\(\d{3}\)\d{3} - \d{4})/
b. /\d{3}-\d{2}-\d{4}/
c. /\w{1,}\s\d{1-2},\s\d{4}/
d. /\d{1-3}\.\d{1-3}\.\d{1-3}/
e. /\d{4}[A-Z]{2}/

"""