def alphabet_position(text):
    alpha = list(''.join(filter(str.isalnum, text.lower())))
    numeric = []
    for a in alpha:
        i = ord(a)
        numeric.append(i-96)
    num_list = ' '.join(map(str, numeric))
    return num_list