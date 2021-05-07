# -*- coding: utf-8 -*-
"""
A simple game of blackjack.
"""
import random
random.seed()

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
 
class Deck:
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.allcards)
        
    def draw_card(self):
        return self.allcards.pop()
    
    def show_deck(self):
        print('The deck has:')
        print(*self.allcards, sep='\n')
    
class Player:
    def __init__(self, total = 100):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.total = total
        self.bet = 0
        
    def add_cards(self, new_card):
        self.cards.append(new_card)
        self.value += values[new_card.rank]
        if new_card.rank == 'Ace':
            self.aces += 1
        
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        
    def win_bet(self):
        self.total += self.bet
        
    def lose_bet(self):
        self.total -= self.bet
        
    def __str__(self):
        return f'Player has {len(self.allcards)} cards.'
    
def take_bet(player):
    while True:
        try:    
            player.bet = int(input('How much would you like to bet? \n'))   
        except ValueError:
            print("Please enter integer values only")
        else:
            if player.bet > player.total:
                print(f'Sorry, your bet cannot exceed your pot of {player.total} chips.')
            else:
                break
            
def hit(player, deck):
    player.add_cards(deck.draw_card())
    player.adjust_for_ace()

def hit_or_stand(player, deck):
    global playing
    while True:
        choice = input('Would you like to hit or stand? \n')
        if choice[0].lower() == 'h':
            hit(player, deck)
        elif choice[0].lower() == 's':
            print('Player stands!')
            playing = False
        else:
            print('Please enter "h" for hit and "s" for stand')
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
    print("\n")
    
def player_busts(player):
    print("Player busts!")
    player.lose_bet()

def player_wins(player):
    print("Player Wins!")
    player.win_bet()

def dealer_busts(dealer):
    print("Dealer busts!")
    dealer.lose_bet()
    player1.win_bet()
    
def dealer_wins(dealer):
    print("Dealer Wins!")
    dealer.win_bet()  
    player1.lose_bet()
    
def push():
    print('Player and Dealer tie!')
    
print('Welcome to BlackJack!') 
while True:
    print('Get as close to 21 as you can without going over!\n\
Dealer hits until she reaches 17. Aces count as 1 or 11. \n')
    game_deck = Deck()
    game_deck.shuffle()
    
    player1 = Player()
    player1.add_cards(game_deck.draw_card())
    player1.add_cards(game_deck.draw_card())
    
    dealer = Player()
    dealer.add_cards(game_deck.draw_card())
    dealer.add_cards(game_deck.draw_card())
    
    show_some(player1, dealer)
    take_bet(player1)
    playing = True
    while playing:
        
        hit_or_stand(player1, game_deck)
        show_some(player1, dealer)
        if player1.value > 21:
            player_busts(player1)
            print(f'Player winnings stand at {player1.total}') 
            break
        
        if player1.value <= 21:
            
            while dealer.value < 17:
                hit(dealer, game_deck)
                
            show_all(player1, dealer)
            
            if dealer.value > 21:
                dealer_busts(dealer)
            elif dealer.value > player1.value:
                dealer_wins(dealer)
            elif dealer.value < player1.value:
                player_wins(player1)
            else:
                push()
        print(f'Player winnings stand at {player1.total}') 
        new_game = input('Would you like to play a new game? Yes or No \n')
        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            playing = False
    break
    
        
        
