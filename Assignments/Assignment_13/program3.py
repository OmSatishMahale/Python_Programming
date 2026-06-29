#Write a program which accept number from user and tell whether it is perfect or not

def Perfect(No):
    Sum = 0

    for i in range(1,No,1):
        if(No % i == 0):
            Sum = Sum + i
    if(Sum == No):
        return True
    else:
        return False
    
def main():
    Value = int(input("ENter the number : "))
    Ret = Perfect(Value)

    if(Ret == True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

if __name__ == "__main__":
    main()