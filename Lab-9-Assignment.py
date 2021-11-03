def addNeighboringLists(list1):
    list2 = []
    for i in range(len(list1)):
        #print(list2)
        if list1[i-1]== list1[len(list1)-1]:
            list2.append(list1[i]+list1[i+1])
        elif i+1 >= len(list1):
            list2.append(list1[i]+list1[i-1])
        else:
            list2.append(list1[i-1]+list1[i]+list1[i+1])
    return list2


def main():
    list1 = [10,20,30,40,50]
    print(addNeighboringLists(list1))
    
main()
    
