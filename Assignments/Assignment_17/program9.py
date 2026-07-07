#Write a program which accept number from user and return number of digit from that number

def CountDigit(No):
    Count = 0

    while(No != 0):
        No = No // 10
        Count = Count + 1

    return Count

def main():
    Value = int(input("Enter the number : "))
    Ret = CountDigit(Value)
    print("Number of Digit from the number is : ",Ret)

if __name__ == "__main__":
    main()