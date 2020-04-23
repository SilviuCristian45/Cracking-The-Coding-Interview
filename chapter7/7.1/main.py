#Design the data structures for a generic deck of cards 
#Explain how you would sub-class it 
#to implement particular card games
from MyClasses import Suit
from MyClasses import Card
import random



    
def GetRandomCard():    
    card_number = random.randint(1,13)
    card_suit_index = random.randint(0,3)
    RandomCard = Card(card_number , Suit(card_suit_index))
    return RandomCard
        
        
def PlayBlackJack():
    print("Welcome to Silviu's Casino")
    print("At the moment , the only game that you are able to play is BlackJack")
    #("Are you ready ? ")
    player_choose = input("Are you ready ? Y/N ")
    player_value = 0
    dealer_value = 0
    
    while player_value <= 21:
        #for dealer
        player_card = GetRandomCard()
        player_card.Print()
        player_value += player_card.number
        #for dealer
        dealer_value += GetRandomCard().number
        
        player_choose = input("Do you want to draw another card ? Y/N ")
        if player_choose == "N":
            break
    
    if player_value > 21:
        print("LOSE . You have more than 21")
    else :
        if player_value == 21:
            print("!!! BlackJack !!!")
        else:
            if player_value > dealer_value:
                print("WIN")
                print("You value "+str(player_value))
                print("Dealer's value "+str(dealer_value))
            else :
                if dealer_value <= 21:
                    print("LOSE")
                    print("You value "+str(player_value))
                    print("Dealer's value "+str(dealer_value))
                else :
                    print("WIN")
                    print("You value "+str(player_value))
                    print("Dealer's value "+str(dealer_value))
            
PlayBlackJack()
        
    




















