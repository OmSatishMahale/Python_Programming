#Write a lambda function using reduce which accept list from user and return maximum from list

from functools import reduce

Maximum = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    
    Data = list()

    Size = int(input("Enter the size of list : "))

    print("ENter the elements of list : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)
    
    RData = reduce(Maximum,Data)
    print("Maximum of all elements of list is : ",RData)

if __name__ == "__main__":
    main()