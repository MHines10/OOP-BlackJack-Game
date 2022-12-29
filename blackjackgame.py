# Black Jack Game Project


# Import the Random Module to create a deck of cards
import random

class Card:
    # gives the cards suit and value
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    # f string to return the reprsentation of a card
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    # create a list to represent a deck of 52 cards with suit and value
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in range(2, 11):
                self.cards.append(Card(suit, value))
            for face in ["Jack", "Queen", "King", "Ace"]:
                self.cards.append(Card(suit, face))
    
    def shuffle(self):
        # shuffles the cards randomly in the list
        random.shuffle(self.cards)
    
    def deal(self):
        # deals the cards by returning the last card in the list and removes it after shuffle
        return self.cards.pop()

class Hand:
    # create an empty list to append cards
    def __init__(self):
        self.cards = []

    # adds cards to the empty list for the players hand
    def add_card(self, card):
        self.cards.append(card)
    
    # removes cards from the deck of cards
    def remove_card(self, card):
        self.cards.remove(card)
    
    # calculates the total of the cards
    def get_value(self):
        value = 0
        ace_count = 0
        for card in self.cards:
            # setting the value of face cards to 10
            if card.value in ["Jack", "Queen", "King"]:
                value += 10

            # setting ace vale to 1 or 11
            elif card.value == "Ace":
                value += 11
                ace_count += 1
            # numbers cards value
            else:
                value += card.value
        
        # If the hand has an ace and its total would put the hand over 21, it will count the Ace as 1
        while value > 21 and ace_count > 0:
            value -= 10
            ace_count -= 1
        
        return value

class Player:
    # takes players name and give and empty hand to accept cards
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
    
    # takes a card from the deck and adds it to the player's hand
    def hit(self, deck):
        self.hand.add_card(deck.deal())
    
    # if player chooses to stand
    def stand(self):
        pass
    
    # if the players hand is over 21
    def bust(self):
        return self.hand.get_value() > 21

# inherits from "Player" class 
class Dealer(Player):
    # sets the dealer name and give dealer an empty hand
    def __init__(self, name):
        super().__init__(name)
    
    # the dealer keeps hitting until the dealer's hand is greater than or equal to 17
    def hit(self, deck):
        while self.hand.get_value() < 17:
            self.hand.add_card(deck.deal())

    
    # dealer stands when their hand is 17 or greater
    def stand(self):
        pass
    
    # if the dealer's hand is over 21 
    def bust(self):
        return self.hand.get_value() > 21

class Game:
    # create a deck of cards, player and dealer
    def __init__(self, player_name):
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Dealer("Dealer")
    
    def play(self):
        # Shuffles the deck of cards
        self.deck.shuffle()
        
        # Deals the first cards
        self.player.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        
        # Shows the player's first cards that were dealt
        print(f"{self.player.name}'s hand: {self.player.hand.cards} ({self.player.hand.get_value()})")
        
        
        # Allow player to choose hit or stand
        while True:
            # take input for player's choice to "Hit" or "Stand"
            choice = input("Would you like to hit or stand? ").lower()

            # if the player chooses to "Hit", deal another card
            if choice == "hit":
                self.player.hit(self.deck)
                print(f"{self.player.name}'s hand: {self.player.hand.cards} ({self.player.hand.get_value()})")

                # Check if the player has "Bust"
                if self.player.bust():
                    # shows dealers hand if player "Bust"
                    print(f"{self.dealer.name}'s hand: {self.dealer.hand.cards} ({self.dealer.hand.get_value()})")
                    print(f"{self.player.name} busts! {self.dealer.name} wins.")
                    return
            # if the player chooses to "Stand"
            elif choice == "stand":
                break
        
        # Dealer's turn
        print(f"{self.dealer.name}'s hand: {self.dealer.hand.cards} ({self.dealer.hand.get_value()})")
        self.dealer.hit(self.deck)
        if self.dealer.bust():
            print(f"{self.dealer.name} busts! {self.player.name} wins.")
            return
        
        # Compare cards value for the score
        if self.player.hand.get_value() > self.dealer.hand.get_value():
            print(f"{self.player.name} wins!")
        elif self.player.hand.get_value() < self.dealer.hand.get_value():
            print(f"{self.dealer.name} wins!")
        else:
            print("It's a tie!")


# Create an Instance of game class to play
player = Game("Monti")
player.play()
