def fib(num):
    a, b = 0, 1
    for i in range(num):
        print(a)
        a, b = b, a + b


def main():
    while True:
        print("Enter a number below 100 to generate fibonacii")
        number=int(input('> '))
        if number<0:
            print("Please enter a positive number")
            return False
        elif number > 100:
            print("Please enter a number below 100")
            return False
        elif 0 < number <= 100:
            break
    fib(number)





if __name__ == '__main__':
    main()
