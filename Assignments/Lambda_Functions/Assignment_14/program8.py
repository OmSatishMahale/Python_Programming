Addition = lambda No1,No2 : No1 + No2

def main():
    Value1 = int(input("ENter First Number : "))
    Value2 = int(input("ENter Second Number : "))

    Ret = Addition(Value1,Value2)
    print("Addition of Two numbers is : ",Ret)

if __name__ == "__main__":
    main()