
#We cannot use elif in Lambda function
Maximum = lambda No1,No2,No3 :No1 if(No1 > No2 and No1 > No3) else(No2 if(No2 > No1 and No2 > No3) else No3)

def main():
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))
    Value3 = int(input("Enter Third Number : "))

    Ret = Maximum(Value1,Value2,Value3)
    print("Maximum number is : ",Ret)

if __name__ == "__main__":
    main()