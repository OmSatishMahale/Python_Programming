#Write a program which takes number from user and print its Table

def Table(No):
    
    for i in range(1,11,1):
        Mul = No * i
        print(Mul)

def main():

    Value = int(input("Enter the number : "))
    Table(Value)

if __name__ == "__main__":
    main()