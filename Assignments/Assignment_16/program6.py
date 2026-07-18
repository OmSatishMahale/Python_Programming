#Write a program which accept number from user and check whether number is positive,negative or zero

def ChkNum(No):
    if(No > 0):
        print("Number is Positive")
    elif(No < 0):
        print("Number is Negative")
    else:
        print("Number is Zero")


def main():
    Value = int(input("Enter the number : "))
    ChkNum(Value)

if __name__ == "__main__":
    main()