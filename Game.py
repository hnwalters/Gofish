from GoFish.Deck import Deck
from random import randint

def main():
    init()

def init():
    computer_hand = []
    human_hand = []
    
    deck = Deck()
    
    for _ in range(5):
        computer_hand.append(deck.deal())
        human_hand.append(deck.deal())
        
    play(computer_hand, human_hand)

def check_four_kind(hand):
    fourkind = [card for card in hand if hand.count(card) == 4]
    if fourkind:
        for card in fourkind:
            hand.pop()
            
            return True
    
    return True
        

def play(computer_hand, human_hand, deck):
    computer_points = 0
    human_points = 0

    turn = 0
    while deck:
        if not human_hand:
            print("Out of cards! You draw 5!")
            for _ in range(5):
                human_hand.append(deck.deal())
                
        if not computer_hand:
            print("Out of cards! I draw 5!")
            for _ in range(5):
                human_hand.append(deck.deal())
        
        if turn%2 == 0:
            print("Your turn!")
            player = human_hand
            opponent = computer_hand
            points = human_points
            
            if check_four_kind(player):
                points += 1
                print("  Point awarded!")
            
            for i in range(human_hand):
                print("    {0}: {1}".format(i, str(human_hand[i])))
            
            guess = int(input("Choose a card index in your hand!\n"))
        else:
            print("My turn!")
            player = computer_hand
            opponent = human_hand
            points = computer_points
            
            if check_four_kind(player):
                points += 1
                print("  Point awarded!")
            
            guess = randint(0, len(computer_hand))
        
        print("  Do you have a {0}?".format(player[guess].value()))
        
        if player[guess] in opponent:
            print("    I have {0} {1}!".format(opponent.count(player[guess]), player[guess].value()))
            
            while player[guess] in opponent:
                player.append(opponent.remove(player[guess]))
        
            if check_four_kind(player):
                points += 1
                print("  Point awarded!")
            
        else:
            print("    Go fish!")
            human_hand.append(deck.deal())
            turn += 1
            
        print("The score is {0} to {1}!".format(human_points, computer_points))
    
    print("The deck is empty!")
    
    if human_points > computer_points:
        print("You win!")
    elif computer_points > human_points:
        print("The computer wins!")
    else:
        print("It's a tie!")
        
if __name__ == '__main__':
    main()