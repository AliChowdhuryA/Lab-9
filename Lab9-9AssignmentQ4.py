
def consInt(num):
    consAdd= 0
    for i in range(num):
        consAdd += i
        print(consAdd)
    return consAdd
        
def main():
    x = int(input("Enter an integer: "))
    consInt(x)

main()
