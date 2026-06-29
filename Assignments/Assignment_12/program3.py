# Write a program which accept two number from user and print its addition,Substraction,Multiplication and Division

def Addition(No1,No2):
    return No1 + No2
def Substraction(No1,No2):
    return No1-No2
def Multiplication(No1,No2):
    return No1*No2
def Division(No1,No2):
    return No1/No2

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("ENter the second number : "))

    Ret1 = Addition(Value1,Value2)
    print("Addition is : ",Ret1)
    Ret2 = Substraction(Value1,Value2)
    print("Substraction is : ",Ret2)
    Ret3 = Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret3)
    Ret4 = Division(Value1,Value2)
    print("Division is : ",Ret4)

if __name__ == "__main__":
    main()