#Write a lambda function using map() which accept list of numbers and return list of sqaure of each number

Square = lambda No : No * No

def main():
    Data = list()

    Size = int(input("Enter size of elements : "))

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    MData = list(map(Square,Data))
    print("Data after Map is : ",MData)

if __name__ == "__main__":
    main()