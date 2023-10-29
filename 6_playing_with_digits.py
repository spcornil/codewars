# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a
# positive integer p
#
# We want to find a positive integer k, if it exists, such that the sum of the digits
# of n taken to the successive powers of p is equal to k * n.
#
# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.

import math

def dig_pow(n, p):
    tot = 0
    for i in str(n):
        tot += int(i)**p
        p = p+1
    if tot/n == math.floor(tot/n):
        return tot/n
    else:
        return -1