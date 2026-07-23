#Design a python application which accept list from user
#Make two threads named as Maximum and Minimum
#Maximum thread should display maximum number from list
#Minimum thread should display minimum number from list
#Accept list from user and pass that list to both threads.

import threading

def Maximum(Data):

    Max = 0

    for no in Data:
        if(no > Max):
            Max = no

    print("Maximum element from list is : ",Max)

def Minimum(Data):

    Min = 0
    
    for no in Data:
        Min = Data[0]
        if(no < Min):
            Min = no
    
    print("Minimum element from list is : ",Min)

def main():

    Arr = list()

    Size = int(input("ENter the Size of list : "))

    print("ENter the elements of list : ")

    for i in range(Size):
        no = int(input())
        Arr.append(no)

    t1 = threading.Thread(target= Maximum,args=(Arr,))
    t2 = threading.Thread(target= Minimum,args=(Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()