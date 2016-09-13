import threading
import multiprocessing as mp
import time


class A:
    #set some value
    def __init__(self,value=0):
        self.value = value
        self.stopped = False
        self.file = open('txt.txt','w')
        
    def print_value(self):
        while True:
            self.file.write(self.value)
            if self.stopped:
                break

    def print_value_plus_1(self):
        while True:
            print(self.value + 1)
            if self.stopped:
                break

    def stop(self):
        self.stopped = True


time_start = time.time()

a = A(1)


p1 = mp.Process(target=a.print_value, name='print_value')
p2 = mp.Process(target=a.print_value_plus_1, name='print_value_plus_1')

p1.start()
p2.start()

while True:
    if time.time() - time_start >= 5: #stop after 5 seconds
        a.stop()
        break
