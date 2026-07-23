#Write a program which contains filter(),Map() and reduce.
# Python application which contains one list of numbers.
# List contains the number which are accepted by user.
# Filter should filter all the Prime number.
# Map function will multiply each number by 2.
# Reduce will return Maximum of all that numbers

from functools import reduce

Prime = lambda No : all(No % i for i in range(2,No))

Square = lambda No : No * 2

Sum = lambda No1,No2  : No1 if (No1 > No2) else No2

def main():
    
    Data = list()

    Size = int(input("Enter the size of list : "))

    print("Enter the elements of list : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    FData = list(filter(Prime,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square,FData))
    print("Data after Map is : ",MData)

    RData = reduce(Sum,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()