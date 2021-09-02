import threading
import time 
import os

def print_odd(n):
    time.sleep(10)
    print("odd :", threading.current_thread().name,os.getpid())
def print_even(n):
    time.sleep(20)
    print("even :", threading.current_thread().name,os.getpid())

if __name__ =="__main__":
    t1=threading.Thread(target=print_odd,args=(100,))
    t2=threading.Thread(target=print_even,args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()
print("bye")
