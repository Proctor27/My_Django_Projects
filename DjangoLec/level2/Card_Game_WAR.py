#The deck is divided evenly,with each player recieving 26 cards,dealt one at a time,
#face down. Anyone may deal first. Each player places his stack of cards face down, in front of him.

#The play

#Each player turns up a card at the same time and the player with the higher card takes both cards and puts them,face down, on the
#bottom of his stack.
#If the cards are the same rank, it is war. Each player turns up three cards face down and one card face up. The player with the higher
#cards takes both piles(six cards). If the turned-up cards are again the same rank, each players places another card face down and turns
#another card face up. The player with the higher card takes all 10 cards, and so on.

#There are some more variations on this but we will keep it simple
#Ignore Double Wars

from random import shuffle

# Two useful variables for creating Cards.

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

#List Comprehension
#mycards = [(s,r) for s in SUITE for r in RANKS]

#FOR LOOPS
"""mycards = []
for r in RANKS:
    for s in SUITE:
        mycards.append((s,r))"""


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate play. You can then use this list of cards to split in half
    and give to the players. It will use SUITE AND RANKS to create the deck, IT should also have a method for splitting/cutting the 
    deck in half and shuffling the deck
    """
        #Initialize play
    def __init__(self):
        print("Creating New Ordered Deck!")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]
    
        #SHUFFLE THE DECK
    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

        #SPLITTING/CUTTING IN HALF
    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])
    
class Hand:
    """
    This is the Hand class. Each player has a hand, and can add or remove cards from that hand. There should be an add and remove
    card method.
    """
    #INITIATE THE HANDS
    def __init__(self,cards):
        self.cards = cards

    #PASS THE CARDS AS STRINGS AND KNOW THE NUMBER OF CARDS A PLAYER HAS
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    #ADD METHOD
    def add(self,added_cards):
        self.cards.extend(added_cards)
        #REMOVE METHOD
    def remove_card(self):
        return self.cards.pop()
    
class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand class object. The player can then play cards and
    check if they still have cards.
    """
    #INITIALIZE THE PLAYER AND HAND
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
    
    #METHOD FOR DRAWN CARDS
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    #METHOD TO REMOVE WAR CARDS
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) <3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
        return war_cards
    def still_has_cards(self):
        """
        Retrun true if player still has cards left
        """
        return len(self.hand.cards) != 0
    
#############################
###### GAME PLAY ############
#############################
print("Welcome to War, Let's begin...")

#Create new deck and split it in half:
d = Deck()
d.shuffle()
half1,half2 = d.split_in_half()

#Create both players
comp = Player("computer",Hand(half1))
name = input("What is your name")
user = Player(name,Hand(half2))

total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings")
    print(user.name+"has the count: "+str(len(user.hand.cards)))
    print(comp.name+"has the count: "+str(len(comp.hand.cards)))
    print("Play a card!")
    print('\n')

    table_cards = []

    c_card = comp.play_card()
    p_card = user.play_card()
    
    table_cards.append(c_card)
    table_cards.append(p_card)
        #CHECKING IF THE RANKS ARE EQUAL IN ORDER TO START A WAR
    if c_card[1] == p_card[1]:
        war_count += 1

        print("War!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
print("Game over, number of rounds:"+str(total_rounds))
print("A war happened "+str(war_count)+" times")
#CHECK TO SEE THE WINNER
print("Does the computer still have cards? ")
print(str(comp.still_has_cards()))
print("Does the human player still have cards? ")
print(str(user.still_has_cards()))