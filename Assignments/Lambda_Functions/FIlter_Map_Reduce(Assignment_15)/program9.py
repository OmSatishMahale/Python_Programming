#Write a lambda function using reduce which accept list of elements and return product of all elements

from functools import reduce

Product = lambda No1,No2 : No1 * No2

def main():
    
    Data = list()
    Size = int(input("Enter the Size of elements : "))

    print("Enter the elements of list : ")
    for i in range(Size):
        no = int(input())
        Data.append(no)

    RData = reduce(Product,Data)
    print("List after reduxe is : ",RData)

if __name__ == "__main__":
    main()