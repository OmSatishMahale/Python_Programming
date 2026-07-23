#Design a python application which accept list from user
#Make two threads named as SUm and Product
#Sum thread should display Sum of number from list
#Product thread should display product of number from list
#Accept list from user and pass that list to both threads.

import threading

def Sum(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no

    print("Sum of Data from list is : ",Sum)

def Product(Data):
    product = 1

    for no in Data:
        product = product * no

    print("Product of all elements from list is : ",product)

def main():

    Arr = list()

    Size = int(input("ENter the Size of list : "))

    print("ENter the elements of list : ")

    for i in range(Size):
        no = int(input())
        Arr.append(no)

    t1 = threading.Thread(target= Sum,args=(Arr,))
    t2 = threading.Thread(target= Product,args=(Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()