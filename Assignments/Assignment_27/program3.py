# Write a Python program to implement a class named Numbers with the following
# specifications:
# • The class should contain one instance variable:
# ◦ Value
# • Define a constructor (__init__) that accepts a number from the user and initializes Value.
# • Implement the following instance methods:
# ◦ ChkPrime() – returns True if the number is prime, otherwise returns False
# ◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
# ◦ Factors() – displays all factors of the number
# ◦ SumFactors() – returns the sum of all factors
# • Create multiple objects and call all methods.

class Numbers():

    def __init__(self,a):
        self.Value = a

    def ChkPrime(self):

        for i in range(2,self.Value+1):
            if(self.Value % i == 0):
                return False
            else:
                return True

    def ChkPerfect(self):

        Sum = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum = Sum + i

        if(Sum == self.Value):
            return True
        else:
            return False

    def Factors(self):

        for i in range(1,self.Value):
            if(self.Value % i == 0):
                print(i)

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum = Sum + i

        return Sum
    
def main():

    nobj = Numbers(6)

    Ret = nobj.ChkPrime()
    if(Ret == True):
        print("Number is Prime")
    else:
        print("Number is not Prime")

    Ret = nobj.ChkPerfect()
    if(Ret == True):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    print("Factors of number is : ")
    nobj.Factors()

    Ret = nobj.SumFactors()
    print("Sum of all factors is : ",Ret)

if __name__ == "__main__":
    main()