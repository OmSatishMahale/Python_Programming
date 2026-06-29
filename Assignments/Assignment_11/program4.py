#Write a program which accept number from user and print Reverse of that number

def PrintReverse(No):
    Reverse = 0
    while(No != 0):
        Digit = No % 10
        Reverse = (Reverse * 10) + Digit
        No = No // 10
    return Reverse

def main():

    Value = int(input("Enter the Number : "))
    Ret = PrintReverse(Value)
    print("Reverse Number is : ", Ret)

if __name__ == "__main__":
    main()