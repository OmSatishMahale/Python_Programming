#List is mutable

def main():
    Marks = [78,90,89,91,88]

    for no in Marks:
        print(no)

    Marks[2] = 86

    print("-"*15)

    for no in Marks:
        print(no)
        
if __name__ == "__main__":
    main()