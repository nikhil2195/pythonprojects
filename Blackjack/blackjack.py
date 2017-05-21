import random

deck = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
values = {'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'10': 10,'Jack': 10,'Queen': 10,'King': 10}

def draw_hand():
    card1 = random.choice(deck)
    card2 = random.choice(deck)
    hand = []
    hand.append(card1)
    hand.append(card2)
    return hand


def hit(hand):
    
    card = random.choice(deck)
    hand.append(card)
    return hand



def evaluate_hand(hand):
    score = 0
    for i in hand:
        if i in values:
            score += values[i]
        else:
            pass
    for x in hand:
        if x == 'Ace':
        
            if score + 11 > 21:
                score += 1
            else:
                score += 11
            
        else:
            pass
    return score


def dealer():
    dealer_hand = draw_hand()
    dealer_score = evaluate_hand(dealer_hand)
    if 'Ace' in dealer_hand:
        dealer_hand=hit(dealer_hand)
        dealer_score=evaluate_hand(dealer_hand)
    
    while dealer_score < 16:
        dealer_hand=hit(dealer_hand)
        dealer_score = evaluate_hand(dealer_hand)
        

    return dealer_hand


def player(dealer_hand):
    player_hand=draw_hand()
    player_score=evaluate_hand(player_hand)
    print("Your Cards: %s " %" ".join(player_hand))
    print("Your Score:",player_score)
    print("Dealer shows: %s" % dealer_hand[0])
    print("Would you like to hit or stand ?")
    a=True
    while a:
           ch=input("> ")
           if ch.lower()=='h':
               player_hand=hit(player_hand)
               player_score=evaluate_hand(player_hand)
               print("Your Cards: %s " %" ".join(player_hand))
               print("Your Score:",player_score)
               print("Dealer shows: %s" % dealer_hand[0])
               
               if player_score >21:
                   a=False
               else:
                   print("Hit or stand ?")
           elif ch.lower()=='s':
               a=False
           else:
               print("Incorrect choice")
    return player_hand
           


def game():
    dealer_hand=dealer()
    player_hand=player(dealer_hand)
    dealer_score=evaluate_hand(dealer_hand)
    player_score=evaluate_hand(player_hand)
    if dealer_score > 21 and player_score <= 21:
        print("```````````````````````````````````````````")
        print(" The dealer's hand: %s" % " ".join(dealer_hand))
        print("The dealer's score: %d" % dealer_score)
        print("Your score: %d" %player_score)
        print(" The dealer went bust!")
        print("```````````````````````````````````````````")
    elif player_score > 21:
        print("```````````````````````````````````````````")
        print("You went bust!")
        print("**You lose!!**")
        print("```````````````````````````````````````````")
    elif dealer_score >= player_score:
        print("```````````````````````````````````````````")
        print(" The dealer's hand: %s" % " ".join(dealer_hand))
        print("The dealer's score: %d" % dealer_score)
        print("Your score: %d" %player_score)
        print("**You lose!!**")
        print("```````````````````````````````````````````")
    else:
        print("```````````````````````````````````````````")
        print(" The dealer's hand: %s" % " ".join(dealer_hand))
        print("The dealer's score: %d" % dealer_score)
        print("Your score: %d" %player_score)
        print("**You win!!**")
        print("```````````````````````````````````````````")
    



def playagain():
   
    while True:
        print("Would you like to play again ? Enter y for Yes and and n for No\n")
        ch=input()
        if ch.lower()=='y':
            print("`````````````````````````````````````````````````")
            game()
        elif ch.lower()=='n':
            print("Thanks for playing")
            print("`````````````````````````````````````````````````")
            break
        else:
            print("Incorrect choice.")
    
    
    

def main():
    print("Welcome to Blackjack")
    print("``````````````````````````````````````````````````````````")
    game()
    playagain()


if __name__=='__main__':
    main()
    
