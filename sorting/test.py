from timer import timer
from sorting.solution import sort
import numpy as np


array1 = np.array([
    1,3,8,4,5,4,7,4,2,8
])

@timer
def test1():
    sorted_array = sort(array1)
    expected_array = np.array([1,2,3,4,4,4,5,7,8,8])
    assert np.array_equal(sorted_array, expected_array), f'expected {expected_array}, actual {sorted_array}'
    print('sorting successful!\n')

array2 = np.random.randint(0, 100, 100)
@timer
def test2():
    sorted_array =  sort(array2)
    print('10^2 elem')

array3 = np.random.randint(0, 100, 1000)
@timer
def test3():
    sorted_array = sort(array3)
    print('10^3 elem')

array4 = np.random.randint(0, 100, 10000)
@timer
def test4():
    sorted_array = sort(array4)
    print('10^4 elem')

if __name__ == "__main__":
    test1()
    test2()
    test3()