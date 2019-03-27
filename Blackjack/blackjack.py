import random
import cards

deck=cards.build_deck()
random.shuffle(deck)
player_hand=[]
dealer_hand=[]

def deal_hand(): #Deals the initial hand
    
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    
    return player_hand,dealer_hand

def hit(hand):  #Adds another card to the hand when hit
    
    card = deck.pop(0)
    hand.append(card)
    return hand



def evaluate_hand(hand): #Evaluates the score of the hand
    score = 0
    for i in hand:
        if i.rank=='Ace':
            if score+i.value>21:
                score=score+1
            else: score=score+11
        else:
            score=score+i.value
    return score

def show(hand):  # Displays the hand
    for i in hand:
        i.print_name()


def player_play(): #Player's turn
    while True:
        print("....................................................")
        print("Enter your choice : h for hit, s for stand ")
        ch = input()

        if ch.lower()=='h':
            hit(player_hand)
            show(player_hand)

        elif ch.lower()=='s':
            break
        else: print("Invalid Choice")
    player_score=evaluate_hand(player_hand)
    return player_hand,player_score




def dealer_play(dealer_hand): #Dealers play

    if dealer_hand[0].rank=='Ace':
        dealer_hand=hit(dealer_hand)
        dealer_score=evaluate_hand(dealer_hand)
    else: dealer_score=evaluate_hand(dealer_hand)    
    
    while dealer_score < 16:
        dealer_hand=hit(dealer_hand)
        dealer_score = evaluate_hand(dealer_hand)
        

    return dealer_hand,dealer_score


def game():
    
    player_hand,dealer_hand=deal_hand()


    print("....................................................")
    print("The dealer shows :")
    dealer_hand[0].print_name()
    print("....................................................")
    print("Your cards are :")
    show(player_hand)

    player_hand,player_score = player_play()
    dealer_hand,dealer_score = dealer_play(dealer_hand)
    print("....................................................")
    print("The dealer's cards are :")
    show(dealer_hand)
    print("....................................................")
    if len(player_hand)>2:
        show(player_hand)



    print("....................................................")
    if player_score>21:
        print("Blackjack !!!!! You win !!!!!")
    elif dealer_score>21:
        print("Dealer went bust !!!!! You win !!!!")

    elif player_score>=dealer_score:
        print(" You win !!!!!!")

    else:
        print("You lose !!!!!!")
    player_hand.clear()
    dealer_hand.clear()


def play_again():
    while True:
        print("Would you like to play again ? [y/n]" )
        ch=input()
        if ch.lower()=='y':
            game()
        elif ch.lower()=='n':
            print("Thank you For PLaying !")
            break
        else: print("Invalid Choice,Please try again ")





def main():
    print("Welcome to Blackjack")
    print("````````````````````````````````````")
    game()
    play_again()



main()