#WRite a python program using multiprocessing.Pool to Calculate
#Sum of all odd numbers from 1 to N 
#Display Process ID,Input Number,Sum of Even Numbers

import multiprocessing
import os

def SumEven(No):
    Sum = 0

    for i in range(1,No+1):
        if(i % 2 != 0):
            Sum = Sum + i

    print(f"Sum of all Odd number from 1 to {No} is : {Sum}")
    print("PRocess ID is : ",os.getpid())

def main():

    Arr = [1000000,2000000,300000]

    pobj = multiprocessing.Pool()
    pobj.map(SumEven,Arr)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()