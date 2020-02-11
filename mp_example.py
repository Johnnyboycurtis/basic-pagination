import time
import multiprocessing as mp
from random import randint, seed
import os


def task(i, conn):
    x = randint(0, 200)
    pid = os.getpid()
    print("{}. (PID: {}) sleeping for {} seconds".format(i, pid, x))
    try:
        time.sleep(x)
        print("{}. (PID: {}) slept for {} seconds".format(i, pid, x))
    finally:
        conn.send((i, pid, x))
        conn.close()




if __name__ == '__main__':
    ctx = mp.get_context() # use system default
    parent_conn, child_conn = mp.Pipe()
    for i in range(10):
        seed(i) # set random state
        p = ctx.Process(target = task, args = (i, child_conn))
        p.start()
        print(parent_conn.recv())
        p.join(5) # terminate after 5 seconds
        p.terminate()