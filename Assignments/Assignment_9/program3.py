#Write a program that takes one number from user and gives the square of that number

def Square(No):
    Square = No * No

    return Square

def main():
    print("Enter number : ")
    Value = int(input())

    Ret = Square(Value)
    print("Square of that number is : ",Ret)

if __name__ == "__main__":
    main()