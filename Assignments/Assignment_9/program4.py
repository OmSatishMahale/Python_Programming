#Write a program that takes one number from user and gives the Cube of that number

def Cube(No):
    Cube = No * No * No

    return Cube

def main():
    print("Enter number : ")
    Value = int(input())

    Ret = Cube(Value)
    print("Cube of that number is : ",Ret)

if __name__ == "__main__":
    main()