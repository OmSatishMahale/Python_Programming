#For every number in the given list, count how many prime number 
# exist between 1 and N using multiprocessing Pool

import multiprocessing

def Prime(No):
    Count = 0

    for i in range(2,No+1):
        flag = True

        for j in range(2,i):
            if(i % j == 0):
                flag = False
                break

        if(flag == True):
            Count = Count + 1

    print(f"Count of Prime Number between {No} is : {Count}")

def main():

    Arr = [1000,2000,3000]

    Result = []

    pobj = multiprocessing.Pool()
    pobj.map(Prime,Arr)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()