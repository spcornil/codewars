# In this little assignment you are given a string of space separated numbers,
# and have to return the highest and lowest number.
# Ex:
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
    

def high_and_low(numbers):
    nums = numbers.split(' ')
    n2 = []
    for n in nums:
        n2.append(int(n))
    n2.sort()
    return f'{n2[-1]} {n2[0]}'