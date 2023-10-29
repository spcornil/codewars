# Given a random non-negative number, you have to return the digits of this
# number within an array in reverse order.

def digitize(n):
    l = [int(i) for i in str(n)]
    return l[::-1]