# Write a program which accepts one number from user and check whether it is prime or not

def CheckPrime(No):

    for i in range(2,No,1):
        if(No % i == 0):
            return False
    return True

def main():
    Value = int(input("Enter the number : "))
    Ret = CheckPrime(Value)

    if(Ret == False):
        print("Number is not Prime")
    else:
        print("Number is Prime")

if __name__ == "__main__":
    main()
