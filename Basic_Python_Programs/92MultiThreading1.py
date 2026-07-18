import threading

def Display():
    print("Inside Display : ",threading.get_ident())    #Gives id of thread

def main():
    print("Inside main : ",threading.get_ident())       #Gives id of thread
    Display()

if __name__ == "__main__":
    main()