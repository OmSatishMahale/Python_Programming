#Write a python program that calculate factorial of varoius
#using Pool.map
#Display process ID,Input Number,Factorial

import multiprocessing
import os

def Factorial(No):

    fact = 1

    for i in range(1, No + 1):
        fact = i * fact

    print("PID of the process is : ",os.getpid())
    print(f"Factorial of {No} is : {fact}")

    return fact

def main():

    Arr = [5,10,12,15]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(Factorial,Arr)

    pobj.close()
    pobj.join()

    print("Factorial of elements from list is : ",Result)

if __name__ == "__main__":
    main()