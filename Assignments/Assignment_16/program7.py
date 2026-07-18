#Write a program which conatins a function name as ChkNum(),pass a number as a parameter to it and print True if divisible by 5 else return false

def ChkNum(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("ENter the number : "))
    Ret = ChkNum(Value)

    print(Ret)

if __name__ == "__main__":
    main()