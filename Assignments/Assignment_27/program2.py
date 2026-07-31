# Write a Python program to implement a class named BankAccount with the following
# requirements:
# • The class should contain two instance variables:
# ◦ Name (Account holder name)
# ◦ Amount (Account balance)
# • The class should contain one class variable:
# ◦ ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
# ◦ Display() – displays account holder name and current balance
# ◦ Deposit() – accepts an amount from the user and adds it to balance
# ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
# (Ensure withdrawal is allowed only if sufficient balance exists)
# ◦ CalculateInterest() – calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# • Create multiple objects and demonstrate all methods.


class BankAccount():
    ROI = 10.5

    def __init__(self,a,b):
        self.Name = a
        self.Amount = b

    def Display(self):
        print(f"Account Holder Name : {self.Name} , Account Balance {self.Amount}")

    def Deposit(self,c):
        self.deposit = c
        self.Amount = self.Amount + self.deposit

        print("AMount after Deposit is : ",self.Amount)

    def WithDraw(self,d):

        self.withdraw = d

        if(self.withdraw > self.Amount):
            print("Insufficient Balance")
        else:
            self.Amount = self.Amount - self.withdraw

        print("Account Balance after withdraw is : ",self.Amount)

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100

        print("Total Interest is : ",Interest)


def main():

    bobj1 = BankAccount("Om",1000000)

    bobj1.Display()
    bobj1.Deposit(100000)
    bobj1.WithDraw(100000)
    bobj1.CalculateInterest()

if __name__ == "__main__":
    main()