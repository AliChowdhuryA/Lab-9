def func(n):

    list1 = [1]

    for i in range(n):
        list1.append(list1[i]+list1[i-1])

    print(list1)
def func2(n):

    list1 = [1]

    for i in range(n):
        list1.append(list1[i]+list1[i-1])

    return list1.pop()

def main():
    n = 0
    print("input an integer: ")
    n = int(input())
    func(n)
    print("The last item in the list is",func2(n))
    

main()
