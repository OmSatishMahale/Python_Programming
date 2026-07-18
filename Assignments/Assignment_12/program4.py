#Write a program which accept a number from user and print that much number starting from 1

def DisplayNo(No):
    
    for i in range(1,No+1,1):
        print(i)

def main():
    Value = int(input("Enter the number : "))
    DisplayNo(Value)

if __name__ == "__main__":
    main()