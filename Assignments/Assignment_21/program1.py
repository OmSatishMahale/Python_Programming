#Design a python application which creates two threads named as prime and non prime
#Accept list from user and pass that list to both threads.
#The prime thread should display all prime number from list
#The non prime thread should display all non prime numbers from list.

import threading


def Prime(Data):
    print("Prime numbers are : ")
    for no in Data:
        if no <= 1:
            continue

        count = 0
        for i in range(2, no):
            if no % i == 0:
                count = count + 1

        if count == 0:
            print(no, end=" ")

def NonPrime(Data):
    print("Non prime numbers are ")

    for no in Data:
        if no <= 1:
            print(no, end=" ")
            continue

        count = 0
        for i in range(2, no):
            if no % i == 0:
                count = count + 1

        if count != 0:
            print(no, end=" ")

def main():
    
    Arr = list()

    Size = int(input("ENter the Size of list : "))

    print("Enter the element of list ")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    t1 = threading.Thread(target=Prime,args=(Arr,))
    t2 = threading.Thread(target=NonPrime,args=(Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()