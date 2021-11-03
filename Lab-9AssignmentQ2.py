#for loop that doubles the persons salary

def doubleDays(numOfDays):
    list1 = [.01]
    TotalAdd = 0.0
    print("Day\tSalary")
    for i in range(numOfDays):
        print(f"{i+1}\t${list1[i]}")
        list1.append(list1[i]*2)
    list1.pop()   
    print(f"Total = ${sum(list1)}")

def main():
    doubleDays(20)

main()
