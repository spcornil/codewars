# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# 
# Here's the deal:
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

import string

def generate_hashtag(s):
    if (len(s) >= 140) or (len(s) == 0):
        return False
    else:
        o = s.lower()
        o2 = string.capwords(o)
        o3 = o2.replace(' ','')
    return f'#{o3}'