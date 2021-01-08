import time


def timer(inner_func, *args, **kwargs):
    """
    times a function, prints function name and execution time in seconds
    """
    start = time.time()
    print(inner_func.__name__)
    inner_func(*args, **kwargs)
    end = time.time()
    print(f"Total time: {end-start} seconds\n")
    return inner_func
