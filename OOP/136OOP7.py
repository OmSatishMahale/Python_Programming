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
        print(Demo.Value1)      
        print(Demo.Value2)      

    #Class Method 
    @classmethod
    def gun(cls):
        print("Inside Class method gun")
        #print(Demo.No1)        #Not Allowed
        #print(Demo.No2)        #Not Allowed
        print(Demo.Value1)      
        print(Demo.Value2)

    #Static Method
    #Cannot access neither class(Optional/may or may not) nor instance variable
    @staticmethod
    def sun():
        print("Inside Static Method sun")
        print(Demo.Value1)      
        print(Demo.Value2)

Demo.sun()