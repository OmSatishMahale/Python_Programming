#Write a lambda function using reduce which accept list from user and return addition of list

from functools import reduce

Addition = lambda No1,No2 : No1 + No2

def main():
    
    Data = list()

    Size = int(input("Enter the size of list : "))

    print("ENter the elements of list : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
    
    RData = reduce(Addition,Data)
    print("Sum of all elements of list is : ",RData)

if __name__ == "__main__":
    main()