import random
import os


def flashCard():
    fr=open('states_capitals.txt','r+')
    questions=fr.readlines()
    question=random.choice(questions)
    question=question.rstrip().split(',')
    state=question[0]
    capital=question[1]

    print("What\'s the capital of ",state," ?" )
    answer=input()
    if answer.lower()==capital.lower():
        print(answer," is the right answer !!")

    else:
        print("Incorect answer ")
        print("The correct answer is ",capital)


def playagain():
    print("`````````````````````````````````````````````````")
    while True:
        print("Would you like to play again ? Enter y for Yes and and n for No\n")
        ch=input()
        if ch.lower()=='y':
            print("`````````````````````````````````````````````````")
            flashCard()
        elif ch.lower()=='n':
            print("Thanks for playing")
            print("`````````````````````````````````````````````````")
            break
        else:
            print("Incorrect choice.")


def main():
    flashCard()
    playagain()

if __name__=='__main__':
    main()
    
