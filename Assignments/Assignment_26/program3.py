# Write a Python program to implement a class named Arithmetic with the following
# characteristics:
# • The class should contain two instance variables: Value1 and Value2.
# • Define a constructor (__init__) that initializes all instance variables to 0.
# • Implement the following instance methods:
# ◦ Accept() – accepts values for Value1 and Value2 from the user.
# ◦ Addition() – returns the addition of Value1 and Value2.
# ◦ Subtraction() – returns the subtraction of Value1 and Value2.
# ◦ Multiplication() – returns the multiplication of Value1 and Value2.
# ◦ Division() – returns the division of Value1 and Value2 (handle division by zero
# properly).
# • Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithematic():

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        print("Enter First Number ")
        self.Value1 = int(input())

        print("Enter Second Number ")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
        return self.Value1 / self.Value2
    
def main():

    aobj = Arithematic()
    aobj.Accept()
    Ret = aobj.Addition()
    print("Addition is : ",Ret)
    Ret = aobj.Substraction()
    print("Substraction is : ",Ret)
    Ret = aobj.Multiplication()
    print("Multiplication is : ",Ret)
    Ret = aobj.Division()
    print("Division is : ",Ret)


if __name__ == "__main__":
    main()