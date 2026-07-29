#Write a python program which accept list of integer and uses pool.map()
# to calculate square of each number in the list. 
# Example I/P :- [1000000,2000000,3000000,4000000]
# O/P :-  [333333833333500000,
# 2666668666667000000,
# ...
# ]

import multiprocessing

def SumSquare(No):

    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + (i ** 2)

    return Sum

def main():

    Arr = [1000000,2000000,3000000]

    Result = []

    pobj = multiprocessing.Pool()

    Result = pobj.map(SumSquare,Arr)

    pobj.close()
    pobj.join()

    print("Sum of all elements from list is : ",Result)

if __name__ == "__main__":
    main()