class Demo:
    
    #Class Variable
    Value1 = 10
    Value2 = 20

    #Instance Variable
    def __init__(self):
        self.No1 = 11
        self.No2 = 21

obj1 = Demo()
obj2 = Demo()

obj1.No1 = 0

print(obj1.No1)
print(obj2.No1)

obj1.Value1 = 0         #Interpreter will create a new instance variable Value1
print(Demo.Value1)