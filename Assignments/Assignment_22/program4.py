#Write a program that calculate 1^5 + 2^5 + 3^5.....+N^5
#using multiprocessing.Pool display execution Time

import multiprocessing
import time

def Sum5(No):

    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + (i ** 5)

    return Sum


def main():

    start_time = time.perf_counter()

    Arr = [1000,2000,3000]

    pobj = multiprocessing.Pool()
    Ret = pobj.map(Sum5,Arr)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()
    print(f"Execution Time is : {end_time - start_time} seconds")

    print("Sum of all elements from list is : ",Ret)

if __name__ == "__main__":
    main()