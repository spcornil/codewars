def disemvowel(string_):
    v = ['a','e','i','o','u','A','E','I','O','U']
    return ''.join([s for s in string_ if s not in v])