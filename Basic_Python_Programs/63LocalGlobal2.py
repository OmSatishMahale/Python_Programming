no = 11

def Display():
    a=21        #local variable
    print("From Display : ",no)
    print("From Display value of a is : ",a)

def Demo():
    print("From Display : ",no)
    print("From Demo value of a is : ",a)       #Error
Display()
Demo()