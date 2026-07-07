#Write a program which accept number from user and return addition of its factors
#I/P = 12
#O/P = 1+2+3+4+6

def Factorial(No):
    
    Sum = 0

    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i
    return Sum

def main():
    Value = int(input("Enter the number : "))
    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()