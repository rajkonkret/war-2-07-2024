import time
import tracemalloc

import numpy as np

# pip install numpy
tracemalloc.start()
array1 = np.arange(10_000_000, dtype=np.int32)
array2 = np.arange(10_000_000, dtype=np.int32)
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Current memory usage: {current / 1024 ** 2} MB; Peak: {peak / 1024 ** 2} MB")

tracemalloc.start()
list1 = list(range(10_000_000))
list2 = list(range(10_000_000))
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Current memory usage: {current / 1024 ** 2} MB; Peak: {peak / 1024 ** 2} MB")


def measure_time(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        tracemalloc.stop()
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024 ** 2} MB; Peak: {peak / 1024 ** 2} MB")
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")

        return result

    return wrapper


@measure_time
def add_without_np():
    # tracemalloc.start()
    res = [list1[i] + list2[i] for i in range(len(list1))]
    # current, peak = tracemalloc.get_traced_memory()
    # tracemalloc.stop()
    # current, peak = tracemalloc.get_traced_memory()
    # print(f"Current memory usage: {current / 1024 ** 2} MB; Peak: {peak / 1024 ** 2} MB")
    #
    return "OK"


@measure_time
def add_np():
    # tracemalloc.start()
    res = array1 + array2
    # current, peak = tracemalloc.get_traced_memory()
    return "Ok"


print("Start")
print(add_without_np())
print(add_np())
