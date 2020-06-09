def linear_search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    last = len(arr) - 1
    found = False

    while first <= last:
        midpoint = (first + last) // 2
        if arr[midpoint] == target:
            return midpoint
        else:
            if target < arr[midpoint]:
                last = midpoint - 1
            else:
                first= midpoint + 1
        

    return -1  # not found
