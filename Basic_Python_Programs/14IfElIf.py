print("-------------------------------------------------------")
print("---------------Ticket Fare System----------------------")
print("-------------------------------------------------------")

print("Enter Your Age")
Age = int(input())

if(Age >=0 and Age <=5):
    print("Free Entry")
elif(Age >=6 and Age<=18):
    print("Your Ticket Fare is : ₹900")
elif(Age >= 19 and Age <= 40):
    print("Your Ticket Fare is : ₹1200")
else:
    print("Your Ticket Fare is : ₹500")
