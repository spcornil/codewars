def get_middle(s):
    p = len(s)//2
    output = ""
    if len(s) % 2 > 0:
        return s[p]
    else:
        l = [s[p-1], s[p]]
        j = ''.join(l)
        return j