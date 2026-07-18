#Write a program which accept number from user and print its factorial

def Factorial(No):
    fact = 1

    for i in range(1,No+1):
        fact = i * fact
    return fact

def main():
    Value = int(input("Enter the number : "))
    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()