# -*- coding: utf-8 -*-
import threading
from queue import Queue
import time
from concurrent.futures import Future

def call_with_future(fn, future, args, kwargs):
    try:
        result = fn(*args, **kwargs)
        future.set_result(result)
    except Exception as exc:
        future.set_exception(exc)

def threaded_return(fn):
    def wrapper(*args, **kwargs):
        future = Future()
        threading.Thread(target=call_with_future, args=(fn, future, args, kwargs)).start()
        return future
    return wrapper
def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class MyClass:
    somevar = 'someval'

    @threaded
    def func_to_be_threaded1(self):
        while True:
            time.sleep(1)
            print(threading.current_thread().getName()+"in t1")

    @threaded
    def func_to_be_threaded2(self):
        while True:
            time.sleep(2)
            print(threading.current_thread().getName()+" in t2")





obj=MyClass()
handle1 = obj.func_to_be_threaded1()

handle2 = obj.func_to_be_threaded2()


handle1.join()
handle2.join()

# # check whether the thread is locked
# print_lock = threading.Lock()
#
# # define worker and thread
# # if there is ONLY 1 thread , 20 jobs should take 10 seconds
# def exampleJob(worker):
#     time.sleep(0.5)
#     with print_lock:
#         print(threading.current_thread().name, worker)
#
# # thread
# def threader():
#     while True:
#         worker =q.get()
#         exampleJob(worker)
#         q.task_done()
#
#
# # make a Queue of workers
# q=Queue()
#
# # generate 10 threads
# for x in range(10):
#     t=threading.Thread(target=threader)
#     t.daemon=True # die when the main thread died
#     t.start()
#
# startTime= time.time() # for performance calculation
#
# # 20 jobs we want to do
# for worker in range(20):
#     q.put(worker)
#
# q.join()
#
# print('Entire job took: ', time.time()-startTime)