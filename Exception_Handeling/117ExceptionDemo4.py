#Generic Except block

def main():
    Ans = 0
    try:
        print("Enter first number : ")
        No1 = int(input())

        print("Enter Second number : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is successfull")

    except ZeroDivisionError as zobj:
        print("Exception occured due to second operand is Zero : ",zobj)

    except ValueError as vobj:
        print("Exception occured due to invalid Data Type : ",vobj)

    #Generic Exception block should always be at the end
    except Exception as eobj:
        print("Exception Occured : ",eobj)
    
    print("Result is : ",Ans)

if __name__ == "__main__":
    main()