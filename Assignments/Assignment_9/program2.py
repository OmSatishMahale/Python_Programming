#Write a program that takes two number from user and gives the greater number and it contain the function named ChkGreater()

def ChkGreater(No1,No2):
    if(No1 > No2):
        return True
    else:
        return False

def main():
    print("Enter number 1 : ")
    Value1 = int(input())

    Value2 = int(input("Enter number 2 : "))

    Ret = ChkGreater(Value1,Value2)

    if(Ret == True):
        print("Number 1 is greater")
    else:
        print("Number 2 is greater")

if __name__ == "__main__":
    main()