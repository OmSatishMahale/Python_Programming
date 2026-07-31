# Write a Python program to implement a class named Circle with the following
# requirements:
# • The class should contain three instance variables: Radius, Area, and Circumference.
# • The class should contain one class variable named PI, initialized to 3.14.
# • Define a constructor (__init__) that initializes all instance variables to 0.0.
# • Implement the following instance methods:
# ◦ Accept() – accepts the radius of the circle from the user.
# ◦ CalculateArea() – calculates the area of the circle and stores it in the Area variable.
# ◦ CalculateCircumference() – calculates the circumference of the circle and stores it in
# the Circumference variable.
# ◦ Display() – displays the values of Radius, Area, and Circumference.
# • Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle():

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circum = 0.0
    
    def Accept(self):
        print("Enter Radius of Circle: ")
        self.Radius = int(input())

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius

    def CalculateCircumference(self):
        self.Circum = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circum)
    
def main():

    cobj = Circle()

    cobj.Accept()
    cobj.CalculateArea()
    cobj.CalculateCircumference()
    cobj.Display()

if __name__ == "__main__":
    main()