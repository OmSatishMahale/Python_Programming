#Write a program which contains filter(),Map() and reduce.
# Python application which contains one list of numbers.
# List contains the number which are accepted by user.
# Filter should filter all the number greater than or equal to 70 and less than or equal to 90.
# Map function will increase number by 10 .
# Reduce will return product of all that numbers

from functools import reduce

FilterX = lambda No : No >= 70 and No <= 90

Increment = lambda No : No + 10

Mul = lambda No1,No2  : No1 * No2

def main():
    
    Data = list()

    Size = int(input("Enter the size of list : "))

    print("Enter the elements of list : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    FData = list(filter(FilterX,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))
    print("Data after Map is : ",MData)

    RData = reduce(Mul,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()