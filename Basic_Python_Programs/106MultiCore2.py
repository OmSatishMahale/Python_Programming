def SumCube(No):
    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + (i ** 3)    #Change
    
    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = SumCube(Value)
    print("Result is : ",Ret)

if __name__ == "__main__":
    main()