class Demo:
    
    #Class Variable
    Value1 = 10
    Value2 = 20

    #Instance Variable
    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    #Instance Method 
    def fun(self):
        print("Inside Instance Method fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)      #Change
        print(Demo.Value2)      #Change

#Call with Object Creation
dobj = Demo()
dobj.fun()