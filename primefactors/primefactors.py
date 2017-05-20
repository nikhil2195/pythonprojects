


def factors(n):
    fact=[]
    for i in range(1,n):
        if n%i==0:
            fact.append(i)
    return fact
    



def checkprime(num):
    if num==1:
        return False
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def primefactor(fact):
    primefact=[]
    for i in fact:
        if checkprime(i):
            primefact.append(i)

    print(primefact)

    
def playagain():
    while True:
        print("Would you like to try again ?[y/n]")
        ch=input()
        if ch.lower()=='y':
            print('````````````````````````````````````````')
            main()
            break
        elif ch.lower()=='n':
            print("The program is terminating")
            break
        else:
            print("Incorrect choice")



def main():
    number=int(input("Enter the number.\n> "))
    x=factors(1210)
    primefactor(x)
    
    

main()




