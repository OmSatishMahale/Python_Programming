def Summation(Data):
    Sum = 0
    
    for no in Data:
        Sum = Sum + no
    
    return Sum

def main():
    Marks = [78,90,89,91,88]
    Ret = Summation(Marks)

    print("Sum of Marks is : ",Ret)
        
if __name__ == "__main__":
    main()