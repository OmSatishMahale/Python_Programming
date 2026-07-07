#Write a program which accept number from user and store it in list and return Minimum

def Minimum(Data):
    
    Min = Data[0]

    for no in Data:
        if(no < Min):
            Min = no

    return Min

def main():
    
    Size = int(input("Enter number of elements : "))
    Data = []

    print("Number of elements : ")
    for no in range(Size):
        no = int(input())
        Data.append(no)

    Ret = Minimum(Data)
    print("Minimum of all elements from list is : ",Ret)

if __name__ == "__main__":
    main()