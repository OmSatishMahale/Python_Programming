#Write a python program which contains one lambda function which accept one parameter and return power of two

Square = lambda No : No ** 2

def main():
    Value = int(input("Enter the number : "))
    Ret = Square(Value)
    print("Value is : ",Ret)

if __name__ == "__main__":
    main()