#WRite a python program using multiprocessing.Pool to Calculate
#Sum of all even numbers from 1 to N 
#Display Process ID,Input Number,Sum of Even Numbers

import multiprocessing
import os

def CountOdd(No):
    Count = 0

    for i in range(1,No+1):
        if(i % 2 != 0):
            Count = Count + 1

    print(f"Count of all Odd number from 1 to {No} is : {Count}")
    print("PRocess ID is : ",os.getpid())

def main():

    Arr = [1000000,2000000,300000]

    pobj = multiprocessing.Pool()
    pobj.map(CountOdd,Arr)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()