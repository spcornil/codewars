#Complete the findNextSquare method that finds the next integral perfect square
# after the one passed as a parameter. Recall that an integral perfect square is
# an integer n such that sqrt(n) is also an integer.
#
#If the parameter is itself not a perfect square then -1 should be returned. You 
# may assume the parameter is non-negative.

import math

def find_next_square(sq):
    if math.sqrt(sq) != math.floor(math.sqrt(sq)):
        return -1
    else:
        return (math.sqrt(sq)+1)**2