#Write a program which accept number from user and store it in list take another input and find frequency of that number from list

def Frequency(Data,No):
    
    freq = 0

    for no in Data:
        if(No == no):
            freq = freq + 1
    
    return freq

def main():
    
    Size = int(input("Enter number of elements : "))
    Value = int(input("ENter number to Search : "))
    Data = []

    print("Number of elements : ")
    for no in range(Size):
        no = int(input())
        Data.append(no)

    Ret = Frequency(Data,Value)
    print("Frequency of number from list is : ",Ret)

if __name__ == "__main__":
    main()