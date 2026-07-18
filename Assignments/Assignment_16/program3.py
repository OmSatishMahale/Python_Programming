#Write a program which conatins a function name as Add(),accept two number from user and return the addition of that number 
def Add(No1,No2):
    return No1+No2

def main():
    Value1 = int(input("ENter the first number : "))
    Value2 = int(input("ENter the second number : "))

    Ret = Add(Value1,Value2)
    print("Addition of two numbers is : ",Ret)

if __name__ == "__main__":
    main()