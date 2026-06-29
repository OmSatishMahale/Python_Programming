# Program to calculate area of circle

def AreaCircle(radius):
    
    Area = 3.14 * radius * radius
    return Area

def main():
    radius = int(input("Enter the radius : "))
    Ret = AreaCircle(radius)
    print("Area of Circle is : ",Ret)

if __name__ == "__main__":
    main()