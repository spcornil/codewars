def elevator_distance(array):
    dist = 0
    for n in range(len(array)-1):
        dist += abs(array[n] - array[n+1])
    return dist