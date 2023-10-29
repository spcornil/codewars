# Your task is to write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...

def series_sum(n):
    sum = 1.00
    for i in range(1, n):
        sum += 1/((i*3)+1)
    if n == 0:
        return '{:.2f}'.format(0)
    else:
        return '{:.2f}'.format(sum)