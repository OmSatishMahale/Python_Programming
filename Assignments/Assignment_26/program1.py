# Write a Python program to implement a class named Demo with the following
# specifications:
# • The class should contain two instance variables: no1 and no2.
# • The class should contain one class variable named Value.
# • Define a constructor (__init__) that accepts two parameters and initializes the instance variables.
# • Implement two instance methods:
# ◦ Fun() – displays the values of instance variables no1 and no2.
# ◦ Gun() – displays the values of instance variables no1 and no2.
# Create two objects of the Demo class as follows:
# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)
# Call the instance methods in the given sequence:
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

class Demo():

    Value = 10

    def __init__(self,a,b):
        self.No1 = a
        self.No2 = b

    def fun(self):
        print(self.No1)
        print(self.No2,"\n")

    def gun(self):
        print(self.No1,)
        print(self.No2,"\n")

def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()

if __name__ == "__main__":
    main()