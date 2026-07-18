def main():
    Ans = 0
    try:
        print("Enter first number : ")
        No1 = int(input())

        print("Enter Second number : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is successfull")

    except Exception as eobj:
        print("Exception Occured : ",eobj)
    
    print("Result is : ",Ans)

if __name__ == "__main__":
    main()