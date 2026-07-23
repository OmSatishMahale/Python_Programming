#Write a python program which contains one lambda function which accept one parameter and return power of two

Multiply = lambda No1,No2 : No1 * No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
    Ret = Multiply(Value1,Value2)
    print("Multiplication is : ",Ret)

if __name__ == "__main__":
    main()