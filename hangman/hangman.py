import random


words = ['ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat', 'clam', 'cobra', 'cougar', 'coyote',
         'crow',
         'deer', 'dog', 'donkey', 'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion', 'lizard',
         'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt', 'otter', 'owl', 'panda', 'parrot', 'pigeon',
         'python',
         'rabbit', 'ram', 'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk', 'sloth', 'snake',
         'spider',
         'stork', 'swan', 'tiger', 'toad', 'trout', 'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'zebra']

searchedword = ''
secret= ''


def main():
    global searchedword,secret
    searchedword=wordSearch()
    secret=hide(searchedword)
    game(searchedword,secret)


def wordSearch():
    return random.choice(words)


def hidden(hide):
    global secret
    for i in range(len(hide)):
        secret= secret + '*'
    return secret


def game(gameword,hiddenword):
    guess=''
    player=0
    print("The searched word is", hiddenword)
    chances=10
    while not chances == 0:
        

        print("Enter your character/word. There are ",chances," guesses remaining.")
        guess=input()
        if guess.lower()==gameword.lower():
            print("Congratulations you've guessed correctly")
            player=1
            break
        if not guess.isalpha():
            print("Please enter a letter or a word")
            continue
        else:
            for i,letter in enumerate(gameword):
                if guess==letter:
                    hiddenword=list(hiddenword)
                    hiddenword[i]=guess
                    hiddenword=''.join(hiddenword)
            if hiddenword.lower()==gameword.lower():
                print("Congratulaions. You've guessed correctly.The secarched word was",hiddenword)
                player=1
                break
            elif hiddenword.lower()!=gameword.lower():
                print("The searched word is",hiddenword)
        chances=chances-1

    if player!=1:
        print("You lose! The searched word was",gameword)




def playagain():
    while True:
        print("Would you like to play again ?[y/n]")
        ch=input()
        if ch.lower()=='y':
            print('````````````````````````````````````````')
            resetGame()
            main()
        elif ch.lower()=='n':
            print("Thanks for playing")
            break
        else:
            print("Incorrect choice")






def main():
    x=wordSearch()
    y=hidden(x)
    game(x,y)
    playagain()



def resetGame():
    global searchedword,secret
    searchedword = ''
    secret=''

if __name__=='__main__':
    main()

