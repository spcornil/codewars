# Write a function that merges two sorted arrays into a single one. The arrays only contain integers.
# Also, the final outcome must be sorted and not have any duplicates.

def merge_arrays(first, second): 
    third = list(set(first + second))
    third.sort()
    return third