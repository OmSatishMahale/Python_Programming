# Write a program which accepts one number and prints its binary equivalent

def Binary(No):

    BinaryNo = 0
    Place = 1

    while(No != 0):
        Digit = No % 2
        BinaryNo = BinaryNo + (Digit * Place)
        Place = Place * 10
        No = No // 2

    return BinaryNo


def main():

    Value = int(input("Enter the Number : "))
    Ret = Binary(Value)
    print("Binary Equivalent is :", Ret)

if __name__ == "__main__":
    main()