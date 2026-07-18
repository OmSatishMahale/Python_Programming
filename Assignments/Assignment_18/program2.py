#Write a program which accept number from user and store it in list and return Maximum

def Maximum(Data):
    
    Max = 0

    for no in Data:
        if(no > Max):
            Max = no

    return Max

def main():
    
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Number of elements : ")
    for no in range(Size):
        no = int(input())
        Data.append(no)

    Ret = Maximum(Data)
    print("Maximum of all elements from list is : ",Ret)

if __name__ == "__main__":
    main()