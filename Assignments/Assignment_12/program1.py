#Write a program which accept one character from user and check whether that character is vowel or consonant.

def CheckVowelConsonant(letter):
    
    if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        return True
    else:
        return False

def main():
    
    char = input("Enter the Character : ")
    Ret = CheckVowelConsonant(char)

    if(Ret == True):
        print("Character is Vowel")
    else:
        print("Character is consonant")


if __name__ == "__main__":
    main()