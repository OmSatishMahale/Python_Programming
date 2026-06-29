def CheckEven(No1):
    if(No1 % 2 == 0):
        print("Number is Even")
    else:
        print("Number is Odd")

def main():
    Value = int(input("Enter Number : "))           #Dual task Execution function
    CheckEven(Value)

if __name__ == "__main__":
    main()