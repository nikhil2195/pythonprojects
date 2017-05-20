def fizzbuzz():
    n=0
    n=int(input("Enter your number \n"))
    if n%3==0 and n%5==0:
        print("Fizzbuzz")
    elif n%3==0:
        print("Fizz")
    elif n%5==0:
        print("Buzz")

fizzbuzz()
