import numpy as np

# def sort(array): # Bubble sort, O(n^2)
#
#     n = len(array)
#     for i in range(n):
#         for j in range(n-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array


def sort(array):  # merge sort, O(nlogn)
    n = len(array)
    if n == 1:
        return array
    else:
        m = n//2
        l = sort(array[:m])
        r = sort(array[m:])
        if r[-1] < l[0]:
            array = np.concatenate((r, l))
        else:
            array = np.concatenate((l, r))
        return array
