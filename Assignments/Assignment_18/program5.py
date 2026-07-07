from MarvellousNum import ChkPrime

def main():
    
    Size = int(input("Enter number of elements : "))

    Data = []

    print("Number of elements : ")
    for no in range(Size):
        no = int(input())
        Data.append(no)

    Ret = ChkPrime(Data)
    print("Sum of all prime numbers is : ",Ret)

if __name__ == "__main__":
    main()