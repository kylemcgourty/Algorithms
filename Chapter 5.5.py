#Chapter 5.5


#5.5.1

answer = """
Codes 3 and 4 are prefix-free and uniquely decodeable.
Code 3 decoding: A.
Code 4 decoding: ADDDD
"""


#5.5.2

answer = "Uniquely decodeable but not prefix free: 1, 10"

#5.5.3

answer = "0011, 011, 11, 1110"

#5.5.4

answer = "The first example is not uniquely decodeable. Let A = 1, B = 00, C = 100000. Then 100000 = ABB0, or C"


#5.5.5

class RunLength:
    def __init__(self, file):
        self.file = file
        self.encoding = list()

    def compress(self):

        count = 0
        old = 1


        while(True):

            bit = self.file[0]

            if (bit != old):
                self.encoding.append(count)
                count = 0
                old = 1 if old == 0 else 0

            count += 1

            if len(self.file) == 1:
                self.encoding.append(count)
                break

            self.file = self.file[1:]

        print(self.encoding)

binary = [1,1,1,1,1,1,0,0,1,1,1,0,1]

encoding = RunLength(binary)

encoding.compress()


#5.5.6

answer = "With run lenght encoding, the size of n would determine then number of bits needed."

#5.5.7

answer = """

Run length encoding: n in binary; Compression ratio length(binary(n))/binary(a)*n
Huffman encoding: 0 * n bits; Compression ratio n bits/binary(a)*n
LWZ: 1 entry in a symbol table; Compression ratio 1 bit/binary(a)*n
"""


#5.5.8

answer = """

a		01100001	
b		01100010

Run length encoding: 124112311 * n
Huffman encoding: 01 * n
LWZ: 1 entry in a symbol table.
"""


#5.5.9

answer = """
Run length compression; probability of sequence have a different character at each position: 1 * 256/257 * 256/257 ... = 1 * (256/257)^(n-1)
When n = 10, the probability is .9617. Let the average bitstream be represented by 11110000. Then it can be represented by two counts of four; four
is represented by 3 bits. Thus the compression ratio would be 6/8. Overall, a random string will have a higher compression ratio when using
the run length methods.

For Huffman encoding, random ASCII characters will construct a trie with lower frequencies of repetitions. As a result, the encodings will 
be near the same length, on average. Let there be 10 random characters in the sample. The height of the Huffman code trie will be ceiling(lg(10)), 
which is 5. Thus each encoding will have between four and five characters. The compression ratio is ~ 4/8 = 50%

For LZW compression, assume 10 random characters are all unique. The constructed codeword table would contain 9 letter combinations, of 
which none would be referred to during the compression. Thus, there would be no compression savings.

"""


#5.5.10 See 5.5.10.pdf

#5.5.11

answer = "A Huffman code for a two character alphabet would only have encodings 1 and 0"

#5.5.13

answer = "The height of the Huffman code would be lg(n), where n is the length of the string."

#5.5.14

answer = "The Huffman code is not unique. The combinations of leaves may be grouped together on different sides."

#5.5.15

answer = "The advantage would lie in quick a tree traversal."

#5.5.16

answer = """
LZW encoding of TOBEORNOTTOBE

TOB
OB
BE
EO
OR
RN
NO
OT

LZW encoding of YABBADAVBADABBADOO

YA
AB
BB
BADO
AD
DAB
AV
OO

LZW encoding of AAAAAAAA

AAAAAAAA
"""