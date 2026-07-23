#Python program which have multiple thread
#Each thread will use the common shared resource(Variable)
#Each thread will increment the value of that variable by 1

import threading
import time

shared_variable = 0
counter_lock = threading.Lock()

def Increment():

    global shared_variable 

    with counter_lock:
        current_value = shared_variable 
        time.sleep(0.1)
        shared_variable = current_value + 1


def main():

    t1 = threading.Thread(target=Increment)
    t2 = threading.Thread(target=Increment)
    t3 = threading.Thread(target=Increment)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("The counter Value is : ",shared_variable)

if __name__ == "__main__":
    main()