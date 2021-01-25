def cocktail_shaker_sort(arr):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
        if swapped == False:
            return arr
        swapped = False
        for i in range(n-1,0,-1):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
    return arr
