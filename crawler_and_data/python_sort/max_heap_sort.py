def max_heap_sort(arr, simulation=False):

    iteration = 0
    if simulation:
        print("iteration",iteration,":",*arr)
        
    for i in range(len(arr) - 1, 0, -1):
        iteration = max_heapify(arr, i, simulation, iteration)

    if simulation:
                iteration = iteration + 1
                print("iteration",iteration,":",*arr)
    return arr


def max_heapify(arr, end, simulation, iteration):

    last_parent = (end - 1) // 2

    # Iterate from last parent to first
    for parent in range(last_parent, -1, -1):
        current_parent = parent

        # Iterate from current_parent to last_parent
        while current_parent <= last_parent:
            # Find greatest child of current_parent
            child = 2 * current_parent + 1
            if child + 1 <= end and arr[child] < arr[child + 1]:
                child = child + 1

            # Swap if child is greater than parent
            if arr[child] > arr[current_parent]:
                arr[current_parent], arr[child] = arr[child], arr[current_parent]
                current_parent = child
                if simulation:
                    iteration = iteration + 1
                    print("iteration",iteration,":",*arr)
            # If no swap occured, no need to keep iterating
            else:
                break
    arr[0], arr[end] = arr[end], arr[0]
    return iteration
