

def checkprime(num):
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            
            return False
    return True



def getnumber(number):
    newnumber = number+1
    while True:

        if not checkprime(newnumber):
            newnumber+=1
        else:
            break
    return newnumber




def main():
    number= 2

    while True:
        answer = input('Would you like to see the next prime? (Y/N)\n')
        if answer.lower().startswith('y'):
            print(number)
            number=getnumber(number)
        else:
            break




if __name__ == '__main__':

    main()
