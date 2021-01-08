from max_subarray_sum.solution import max_subarray_sum

def test1():
    array = [-1, 2, 4, -3, 5, 2, -5, 2]
    subarray_sum = max_subarray_sum(array)
    assert subarray_sum == 10, f'expected: 10, actual: {subarray_sum}'


if __name__ == "__main__":
    test1()