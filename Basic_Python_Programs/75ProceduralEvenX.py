def CheckEven(No1):
    if(No1 % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter Number : "))           #Dual task Execution function
    Ret = CheckEven(Value)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()