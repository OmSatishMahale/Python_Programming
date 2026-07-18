Minimum = lambda No1,No2 : No1 if (No1 < No2) else No2 

def main():
    Value1 = int(input("Enter the First number : "))
    Value2 = int(input("Enter the Second number : "))
    Ret = Minimum(Value1,Value2)

    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()