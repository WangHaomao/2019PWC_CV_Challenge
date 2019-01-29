import multiprocessing
from multiprocessing import Process
from time import sleep
import os
def ope():


    print('123')
    sleep(5)
    print('still running')
    print('789')

if __name__ == '__main__':

    for i in range(10):
        p = Process(target=ope)

        p.start()
        # p.join()
        print(p.pid)
        # print(','+str(os.getuid()))
    print('niubi')