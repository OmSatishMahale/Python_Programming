#Write a program which accept number from user and return number of digit from that number

def CountDigit(No):
    Count = 0
    Sum = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter the number : "))
    Ret = CountDigit(Value)
    print("Sum of Digit from the number is : ",Ret)

if __name__ == "__main__":
    main()