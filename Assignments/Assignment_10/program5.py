# Write a program which accept one number from user and print all the odd numbers till that number

def PrintOdd(No):
    for i in range(1,No+1,1):
        if(i % 2 != 0):
            print(i)

def main():
    Value = int(input("Enter the number : "))
    PrintOdd(Value)

if __name__ == "__main__":
    main()