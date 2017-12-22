# -*- coding: utf-8 -*-
import  multiprocessing

# def spawn(num,num2):
#     print('Spawned! {0}{1}'.format(num,num2))


# if __name__ =='__main__':
#     for i in range(100):
#         p=multiprocessing.Process(target=spawn, args=(i,i+1))
#         p.start()
#         p.join() # when join will wait for the process before it

def job(num):
    return  num*2

if __name__=='__main__':
    p= multiprocessing.Pool(processes=20)
    data=p.map(job ,range(10))
    data2 = p.map(job, range(20))
    p.close()
    print(data)
    print(data2)