
    def compare(arr, reverse):
        n = len(arr)//2
        for i in range(n):
            if reverse != (arr[i] > arr[i+n]):
                arr[i], arr[i+n] = arr[i+n], arr[i]
        return arr

    def bitonic_merge(arr, reverse):
        n = len(arr)
        
        if n <= 1:
            return arr
        
        arr = compare(arr, reverse)
        left = bitonic_merge(arr[:n // 2], reverse)
        right = bitonic_merge(arr[n // 2:], reverse)
        return left + right
    
    #end of function(compare and bitionic_merge) definition
    n = len(arr)
    if n <= 1:
        return arr
    # checks if n is power of two
    if not (n and (not(n & (n - 1))) ):
        raise ValueError("the size of input should be power of two")
    
    left = bitonic_sort(arr[:n // 2], True)
    right = bitonic_sort(arr[n // 2:], False)

    arr = bitonic_merge(left + right, reverse)
        
    return arr
