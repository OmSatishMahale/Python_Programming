#Write a python program which creates two different threads as EVen and odd
#EVen thread should Display first 10 even numbers
#Odd thread should Display first 10 odd numbers
#Both thread should execute independently using threadng module

import threading

def Even(No):
    
    for i in range(1,No):
        if(i % 2) == 0:
            print("EVen numbers are : ",i)

def Odd(No):
    for i in range(1,No):
        if(i % 2) != 0:
            print("Odd numbers are : ",i)

def main():
    
    t1 = threading.Thread(target=Even,args=(11,))
    t2 = threading.Thread(target=Odd,args=(11,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()