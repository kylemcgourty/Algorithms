#Chapter 2.2


#2.2.1

i = 0
j = 5


aux = "A E Q S U Y E I N O S T"

"""TABLE:
   i  j    a
   0       A
   1       A E 
      5    A E E
      6    A E E I
      7    A E E I N
      8    A E E I N O
   2       A E E I N O Q
   3       A E E I N O Q S
      9    A E E I N O Q S S
      10   A E E I N O Q S S T
   4       A E E I N O Q S S T Y   

"""



#2.2.2
answer = "topdown mergesort"
"""                  a = E A S Y Q U E S T I O N
        
merge(a, 0, 0, 1)    a = A E
merge(a, 2, 2, 3)    a =     S Y
merge(a, 0, 1, 3)    a = A E S Y
merge(a, 4, 4, 5)    a           Q U
merge(a, 6, 6, 7)    a =             E S
merge(a, 4, 5, 7)    a =         E Q S U
merge(a, 0, 3, 7)    a = A E E Q S S U Y
merge(a, 8, 8, 9)    a =                 I T
merge(a, 10, 10, 11) a =                     N O
merge(a, 8, 9, 11)   a =                 I N O T
merge(a, 0, 5, 11)   a = A E E I N O Q S S T U Y
"""

#2.2.3
answer = "bottomup mergesort"

"""                  a = E A S Y Q U E S T I O N

merge(a, 0, 0, 1)    a = A E
merge(a, 2, 2, 3)    a =     S Y
merge(a, 4, 4, 5)    a           Q U
merge(a, 6, 6, 7)    a =             E S
merge(a, 8, 8, 9)    a =                 I T
merge(a, 10, 10, 11) a =                     N O
merge(a, 0, 1, 3)    a = A E S Y
merge(a, 4, 5, 7)    a =         E Q S U
merge(a, 8, 9, 11)   a =                 I N O T
merge(a, 0, 3, 7)    a = A E E Q S S U Y
merge(a, 0, 5, 11)   a = A E E I N O Q S S T U Y
"""

#2.2.4

answer = "Yes. Otherwise as sorting proceeds, a small key may occur later on in the unordered subarray." \
         "As a result, the output would not be in sorted order."

#2.2.5

"""
Top down
Subarray lengths: 2, 4, 8, 16, 32, 39.

Bottom up
Subarray lengths: 2, 4, 8, 16, 32, 39

"""