# Write a program which accept one number from user and print all the even numbers till that number

def PrintEven(No):
    for i in range(1,No+1,1):
        if(i % 2 == 0):
            print(i)

def main():
    Value = int(input("Enter the number : "))
    PrintEven(Value)

if __name__ == "__main__":
    main()