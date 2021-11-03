vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"

def VandChecker(string1):
    v=0
    c=0
    for i in string1:
        if i in vowels:
            v+=1
        elif i in consonants:
            c+=1
    print("vowels: ", v)
    print("consonants: ", c)


def main():
    s = ''
    s = input("Input a string: ")
    VandChecker(s)
main()
