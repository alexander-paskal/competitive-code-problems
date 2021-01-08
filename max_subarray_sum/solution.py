# def max_subarray_sum(array):  # O(n^3)
#
#     n = len(array)
#     best_sum = 0
#     for i in range(n):
#         for j in range(i, n):
#             sum = 0
#             for k in range(i, j):
#                 sum += array[k]
#             if sum > best_sum:
#                 best_sum = sum
#
#     return best_sum

#
# def max_subarray_sum(array):  # O(n^2)
#
#     n = len(array)
#     best_sum = 0
#     for i in range(n):
#         sum = 0
#         for j in range(i, n):
#             sum += array[j]
#             best_sum = max(best_sum, sum)
#
#     return best_sum


def max_subarray_sum(array):  # O(n)

    n = len(array)
    best_sum = 0
    sum = 0
    for i in range(n):
        sum = max(array[i], sum+array[i])
        best_sum = max(best_sum, sum)

    return best_sum

def main():
    array_str = input()
    array = [int(char) for char in array_str.split(', ')]
    print(max_subarray_sum(array))


if __name__ == "__main__":
    main()