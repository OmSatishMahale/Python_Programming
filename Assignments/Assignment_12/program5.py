#Write a program which accept a number from user and print that much number in reverse order

def DisplayRevNo(No):
    
    for i in range(No,0,-1):
        print(i)

def main():
    Value = int(input("Enter the number : "))
    DisplayRevNo(Value)

if __name__ == "__main__":
    main()