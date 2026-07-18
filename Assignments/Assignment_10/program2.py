#Write a program which takes number from user and print sum of N numbers

def Summation(No):
    
    Sum = 0
    for i in range(1,No+1,1):
        Sum = Sum + i
    print("Sum of all N numbers is : ",Sum)

def main():

    Value = int(input("Enter the number : "))
    Summation(Value)

if __name__ == "__main__":
    main()