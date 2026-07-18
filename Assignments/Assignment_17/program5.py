#Write a program which accept one number from user and check whether number is prime or not

def ChkPrime(No):

    for i in range(2,No):
        if(No % i == 0):
            return False
        else:
            return True
        
def main():
    Value = int(input("Enter the number : "))
    Ret = ChkPrime(Value)

    if(Ret == True):
        print("NUmber is Prime")
    else:
        print("Number is not PRime")

if __name__ == "__main__":
    main()