
def pigeonhole_sort(arr):
    Max = max(arr)
    Min = min(arr)
    size = Max - Min + 1

    holes = [0]*size

    for i in arr:
        holes[i-Min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + Min
            i += 1
    return arr
