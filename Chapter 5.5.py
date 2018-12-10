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