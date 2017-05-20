import random



def guessNumber():
    number=random.randint(1,20)
    count=0

    while count<=5:

        try:
            choice=int(input("Guess the number\n"))
        except ValueError:
            print("Please enter a number")


        if choice ==number:
            break
        elif choice > number:
            print("you're a little higher")

        elif choice < number:
            print("you're a little lower")
        count += 1
    if choice==number:
        print("You've guessed the number correctly\n")
    elif choice!=number:
        print("The number is incorrect.You've run out of guesses\n")
    print("Would you like to play again ?\nEnter y for Yes and n for No")
    ch=input()
    while True:
        if ch.lower()=='y':
            print("`````````````````````````````````````````````````")
            guessNumber()
        elif ch.lower()=='n':
            print("Thanks for playing")
            print("`````````````````````````````````````````````````")
            break
        else:
            print("Incorrect choice")

def main():
    print("Enter your name")
    name=input()
    print("Hello",name)
    print("I have chosen a number between 1,20.\nCan you guess the number ?")
    guessNumber()
    




if __name__ == '__main__':
    main()
