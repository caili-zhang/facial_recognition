# -*- coding: utf-8 -*-
import threading
from queue import Queue
import time

# check whether the thread is locked
print_lock = threading.Lock()

# define worker and thread
# if there is ONLY 1 thread , 20 jobs should take 10 seconds
def exampleJob(worker):
    time.sleep(0.5)
    with print_lock:
        print(threading.current_thread().name, worker)

# thread
def threader():
    while True:
        worker =q.get()
        exampleJob(worker)
        q.task_done()


# make a Queue of workers
q=Queue()

# generate 10 threads
for x in range(10):
    t=threading.Thread(target=threader)
    t.daemon=True # die when the main thread died
    t.start()

startTime= time.time() # for performance calculation

# 20 jobs we want to do
for worker in range(20):
    q.put(worker)

q.join()

print('Entire job took: ', time.time()-startTime)