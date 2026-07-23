# Design a Python application that creates two threads named Thread1 and Thread2.
# Thread1 should display numbers from 1 to 50.
# Thread2 should display numbers from 50 to 1 in reverse order.
# Ensure - 
# Thread2 starts execution only after Thread1 has completed.
# Use appropriate thread synchronization

import threading

def Order(No):
    
    for no in range(1,No+1):
        print(no,sep=" ")

print("\n")

def ReverseOrder(No):
    
    for no in range(No,0,-1):
        print(no,)

def main():
    
    t1 = threading.Thread(target=Order,args=(50,))
    t2 = threading.Thread(target=ReverseOrder,args=(50,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()