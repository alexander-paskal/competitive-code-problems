from max_subarray_sum.solution import max_subarray_sum
import time
import numpy as np


def timer(inner_func, *args, **kwargs):
    start = time.time()
    print(inner_func.__name__)
    inner_func(*args, **kwargs)
    end = time.time()
    print(f"Total time: {end-start} seconds")
    return inner_func

array1 = [-1, 2, 4, -3, 5, 2, -5, 2]

@timer
def test1():

    subarray_sum = max_subarray_sum(array1)
    assert subarray_sum == 10, f'expected: 10, actual: {subarray_sum}'
    print('test 1 successful!')

array2 = np.random.randint(-10, 10, 100)
@timer
def test2():
    max_subarray_sum(array2)
    print('test 2 successful!')


array3 = np.random.randint(-10, 10, 500)
@timer
def test3():
    max_subarray_sum(array3)
    print('test 3 successful!')


if __name__ == "__main__":
    test1()
    print('Success!!!')