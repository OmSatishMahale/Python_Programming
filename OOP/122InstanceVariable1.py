class Marvellous:
    
    No1 = 11                #Class Variable (limbu,kanda)
    No2 = 12                #Class Variable (limbu,kanda)

    def __init__(self):
        self.Value1 = 21    #Instance Variable
        self.Value2 = 51    #Instance Variable

print(Marvellous.No1)
print(Marvellous.No2)

#Object/Instance Creation
mobj1 = Marvellous()        
mobj2 = Marvellous()
mobj3 = Marvellous()

print(mobj1.Value1)
print(mobj2.Value1)