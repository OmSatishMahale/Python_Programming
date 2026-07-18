#Write a program which accepts one number from user and print its sum

def PrintSum(No):

    Sum = 0
    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter number : "))
    Ret = PrintSum(Value)
    print("Sum of Number is : ",Ret)

if __name__ == "__main__":
    main()