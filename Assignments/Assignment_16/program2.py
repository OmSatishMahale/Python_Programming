#Write a program which conatins a function name as ChkNum(),pass a number as a parameter to it and print it is even number or odd number

def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("ENter the number : "))
    Ret = ChkNum(Value)

    if(Ret == True):
        print("Number is even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()