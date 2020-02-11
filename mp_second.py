from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    return x*x

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=2) as pool:

        # evaluate "f(20)" asynchronously
        #res = pool.apply_async(f, range(10000))      # runs in *only* one process
        #print(res.get(timeout=1))             # prints "400"
        res = pool.map_async(f, range(10000))
        total = sum(res.get(timeout=1))
        print("total: ", total)