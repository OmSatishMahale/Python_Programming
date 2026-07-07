#Create one module named as Marvellous which contains addition,substraction,multiplication and division and call it from one program

from Marvellous import *

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter Second number : "))

    Ret = Addition(Value1,Value2)
    print("Addition is : ",Ret)

    Ret = Subtraction(Value1,Value2)
    print("Substraction is : ",Ret)

    Ret = Multiplication(Value1,Value2)
    print("Multiplication is : ",Ret)

    Ret = Division(Value1,Value2)
    print("Division is : ",Ret)

if __name__ =="__main__":
    main()