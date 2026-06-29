def CheckEven(No1):
    return(No1 % 2 == 0)

def main():
    Value = int(input("Enter Number : "))          
    Ret = CheckEven(Value)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()