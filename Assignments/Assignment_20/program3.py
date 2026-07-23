#Design a python program which contains two thread evenlist and oddlist
#Accept a list of numbers from user 
#Evenlist thread should extract all even numbers from list and display its sum
#Oddlist thread should extract all odd numbers from list and display its sum


import threading

def EvenList(Data):
    Sum = 0
    for no in Data:
        if no % 2 == 0:
            Sum = Sum + no
    print("Sum of all EVen elements is : ", Sum, flush=True)


def OddList(Data):
    Sum = 0

    for no in Data:
        if no % 2 != 0:
            Sum = Sum + no
    print("Sum of all Odd elements is : ", Sum, flush=True)

def main():
    Arr = list()

    print("Enter the Size of list : ", end="", flush=True)
    Size = int(input())

    print("Enter the elements of list : ", flush=True)
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    t1 = threading.Thread(target=EvenList,args=(Arr,))
    t2 = threading.Thread(target=OddList,args=(Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()