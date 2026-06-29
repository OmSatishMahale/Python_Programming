# Program to calculate area of rectangle

def AreaRectangle(len,wid):
    
    Area = len * wid
    return Area

def main():
    
    length = int(input("Enter the length : "))
    Width = int(input("Enter the Width : "))

    Ret = AreaRectangle(length,Width)
    print("Area of Rectangle is : ",Ret)

if __name__ == "__main__":
    main()