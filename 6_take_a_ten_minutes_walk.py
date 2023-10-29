# Input array represents a block walked in a particular direction. (eg. ['n', 's', 'w', 'e']).
# Create a function that returns true if walking 10 blocks AND returns you to original position.

# First pass solution
def is_valid_walk(walk):
    count_n = 0
    count_s = 0
    count_e = 0
    count_w = 0
    if len(walk) != 10:
        return False
    else:
        for w in walk:
            if w == 'n':
                count_n += 1
            if w == 's':
                count_s += 1
            if w == 'e':
                count_e += 1
            if w == 'w':
                count_w += 1
    return (count_n == count_s) and (count_e == count_w)

# More concise solution
def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    elif walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w'):
        return True
    else:
        return False