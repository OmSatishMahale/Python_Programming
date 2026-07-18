#Write a program which accept number from user and store it in list and return

def Addition(Data):
    
    Sum = 0

    for no in Data:
        Sum = Sum + no

    return Sum

def main():
    
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Number of elements : ")
    for no in range(Size):
        no = int(input())
        Data.append(no)

    Ret = Addition(Data)
    print("Sum of all elements from list is : ",Ret)

if __name__ == "__main__":
    main()