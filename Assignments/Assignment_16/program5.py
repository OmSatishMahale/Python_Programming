#Write a program which prints 10 9 8 7 6 5 4 3 2 1 On Screen

def Display():

    for i in range(10, 0, -1):
        print(i, end=' ')

def main():
    Display()

if __name__ == "__main__":
    main()