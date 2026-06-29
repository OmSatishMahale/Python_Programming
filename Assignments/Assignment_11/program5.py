#CHeck Whether number is Palindrome or not

def CheckPalindrome(No):

    temp = No
    Reverse = 0

    while(No != 0):
        Digit = No % 10
        Reverse = (Reverse * 10) + Digit
        No = No // 10

    if(temp == Reverse):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))
    Ret = CheckPalindrome(Value)

    if(Ret == True):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

if __name__ == "__main__":
    main()