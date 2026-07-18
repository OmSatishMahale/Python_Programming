import multiprocessing
import time
import os

#2 + 4 + 6 + 8 = 20
def SumEven(No):

    print(f"PID of SumEven is : {os.getpid()} PPID of SumEven is : {os.getppid()}")
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i
    print("Summation of Even is : ",Sum)

#1 + 3 + 5 + 7 + 9 = 25
def SumOdd(No):

    print(f"PID of SumOdd is : {os.getpid()} PPID of SumOdd is : {os.getppid()}")
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i
    print("Summation of Odd is : ",Sum)

def main():

    print(f"PID of Main is : {os.getpid()} PPID of main is : {os.getppid()}")
    start_time = time.perf_counter()
    t1 = multiprocessing.Process(target = SumEven,args=(100,))
    t2 = multiprocessing.Process(target = SumOdd,args=(100,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    end_time = time.perf_counter()

    print(f"Time required {end_time - start_time:.4f} sec")

if __name__ == "__main__":
    main()