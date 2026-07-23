#Design a python program which contains three thread small,Capital and Digits
#Accept a string from user 
#small thread should extract all small letters from string and display its count
#Capital thread should extract all capital letters from string and display its count
#Digits thread should extract all digits from string and display its count
#Each thread must also display thread id and name of thread


import threading

def Small(String):
    
    Count = 0
    for str in String:
        if str >= "a" and str <= "z":
            Count = Count + 1
    print("Count of all small character is : ",Count)
    print("Thread id is : ",threading.get_ident())
    print("Current thread name is : ",threading.current_thread().name)


def Capital(String):
    
    Count = 0
    for str in String:
        if str >= "A" and str <= "Z":
            Count = Count + 1
    print("Count of all Capital character is : ",Count)
    print("Thread id is : ",threading.get_ident())
    print("Current thread name is : ",threading.current_thread().name)

def Digits(String):
    
    Count = 0
    for str in String:
        if str >= "0" and str <= "9":
            Count = Count + 1
    print("Count of all Digits is : ",Count)
    print("Thread id is : ",threading.get_ident())
    print("Current thread name is : ",threading.current_thread().name)

def main():

    char = input("Enter the String : ")


    t1 = threading.Thread(target=Small,args=(char,))
    t2 = threading.Thread(target=Capital,args=(char,))
    t3 = threading.Thread(target=Digits,args=(char,))

    print("Thread id is : ",threading.get_ident())
    print("Current thread name is : ",threading.current_thread().name)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()