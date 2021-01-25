def min_heap_sort(arr, simulation=False):

    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)

    for i in range(0, len(arr) - 1):
        iteration = min_heapify(arr, i, simulation, iteration)

    return arr


def min_heapify(arr, start, simulation, iteration):

    # Offset last_parent by the start (last_parent calculated as if start index was 0)
    # All array accesses need to be offset by start
    end = len(arr) - 1
    last_parent = (end - start - 1) // 2

    # Iterate from last parent to first
    for parent in range(last_parent, -1, -1):
        current_parent = parent

        # Iterate from current_parent to last_parent
        while current_parent <= last_parent:
            # Find lesser child of current_parent
            child = 2 * current_parent + 1
            if child + 1 <= end - start and arr[child + start] > arr[
                child + 1 + start]:
                child = child + 1

            # Swap if child is less than parent
            if arr[child + start] < arr[current_parent + start]:
                arr[current_parent + start], arr[child + start] = \
                    arr[child + start], arr[current_parent + start]
                current_parent = child
                if simulation:
                    iteration = iteration + 1
                    print("iteration", iteration, ":", *arr)
            # If no swap occured, no need to keep iterating
            else:
                break
    return iteration
