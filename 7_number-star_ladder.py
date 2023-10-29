def pattern(n):
    s = ""
    for i in range(n):
        s += "1" + "*"*i + str(i+1) + "\n"
    return s[1:-1]
