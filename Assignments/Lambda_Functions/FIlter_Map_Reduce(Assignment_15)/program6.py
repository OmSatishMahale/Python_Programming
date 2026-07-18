#Write a lambda function using reduce which accept list from user and return minimum from list

from functools import reduce

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2

def main():
    
    Data = list()

    Size = int(input("Enter the size of list : "))

    print("ENter the elements of list : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
    
    RData = reduce(Minimum,Data)
    print("Minimum of all elements of list is : ",RData)

if __name__ == "__main__":
    main()