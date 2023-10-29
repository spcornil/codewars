# Given the triangle of consecutive odd numbers:
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1)

def row_sum_odd_numbers(n):
    row = []
    s = (n*n)-(n-1)
    f = s + n * 2
    for i in range(s, f, 2):
        row.append(i)
    return sum(row)