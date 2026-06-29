CheckEven = lambda No1 : (No1 % 2 == 0)

def main():
    Value = int(input("Enter Number : "))          
    Ret = CheckEven(Value)                  #Ret = (Value % 2 == 0)

    if(Ret == True):
        print("Number is Even")
    else:
        print("Number is Odd")

if __name__ == "__main__":
    main()