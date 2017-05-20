def bubblesort(sortlist):

    l=len(sortlist)
    for i in range(l):
        for j in range(i+1,l):
            if sortlist[i]>sortlist[j]:
                sortlist[i],sortlist[j]=sortlist[j],sortlist[i]

    return sortlist

def main():
    print("Enter the list cof numbers to be sorted.Keep a space between the numbers")
    numbers=input()
    sortlist=list(map(int, numbers.split()))
    sortedlist=bubblesort(sortlist)
    print(sortedlist)


main()
