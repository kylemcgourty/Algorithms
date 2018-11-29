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