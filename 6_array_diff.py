# Your goal in this kata is to implement a difference function, which subtracts
# one list from another and returns the result.
#
# It should remove all values from list a, which are present in list b keeping
# their order.
#
# array_diff([1,2],[1]) == [2]
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(a, b):
    #return [i for i in a if i not in b]
    output = []
    for i in a:
        if i not in b:
            output.append(i)
    return output