#Write a program which contains filter(),Map() and reduce.
# Python application which contains one list of numbers.
# List contains the number which are accepted by user.
# Filter should filter all the even number.
# Map function will square number.
# Reduce will return sum of all that numbers

from functools import reduce

Even = lambda No : No % 2 == 0

Square = lambda No : No * No

Sum = lambda No1,No2  : No1 + No2

def main():
    
    Data = list()

    Size = int(input("Enter the size of list : "))

    print("Enter the elements of list : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    FData = list(filter(Even,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square,FData))
    print("Data after Map is : ",MData)

    RData = reduce(Sum,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()