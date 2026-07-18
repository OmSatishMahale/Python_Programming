#Write a program which accepts number from user and print the number of Digit from that number

def CountDigits(No):
    Count = 0

    while(No != 0):
        No = No // 10
        Count = Count + 1
    return Count

def main():

    Value = int(input("Enter the number : "))
    Ret = CountDigits(Value)
    print("Number of Digit in number is : ",Ret)

if __name__ == "__main__":
    main()