import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return (f'{self.rank} of {self.suit}')

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)

    def adjust_for_ace(self):
        self.value = 0
        for card in self.cards:
            if card.rank != 'Ace':
                self.value=self.value+values[card.rank]
            else :
                self.aces=self.aces+1
                if self.value<11:
                    self.value=self.value+values[card.rank]
                else:
                    self.value=self.value+1

def take_bet(total=100):

    while True:
        try:
            print(f'You have {total} in your wallet')
            bet=int(input('Enter your betting amount'))
        except:
            print('Enter a valid bet')
        else:
            if bet<=total:
                return bet
            else:
                print('Enter a valid bet less than total')
                continue
from IPython.display import clear_output
def show_some(player,dealer):
    clear_output()
    for card in player:
        print(f'Player : {card}')
    print(f'Dealer : {dealer[0]}')

def show_all(player,dealer):
    clear_output()
    for card in player:
        print(f'Player :{card}')
    for card in dealer:
        print(f'Dealer :{card}')

def player_hit_stand(deck,player_hand,dealer_hand):
    loop=True
    while loop:
        if player_hand.value<21:
            x=input('Player: Do you wish to Hit enter h or Stand then press s')
            if x=='h':
                px=deck.deal()
                player_hand.add_card(px)
                player_hand.adjust_for_ace()
                show_some(player_hand.cards,dealer_hand.cards)
            else:
                loop=False
        else:
            loop=False
    return (deck,player_hand)

def dealer_hit_stand(deck,player_hand,dealer_hand):
    loop=True
    while loop:
        if dealer_hand.value < 17:
            dx=deck.deal()
            dealer_hand.add_card(dx)
            dealer_hand.adjust_for_ace()
            show_all(player_hand.cards,dealer_hand.cards)
        else:
            show_all(player_hand.cards,dealer_hand.cards)
            loop=False
    return (deck,dealer_hand)

def player_bust(hand,bet,amount):
    if hand.value>21:
        amount=amount-bet
        show_all(player_hand.cards,dealer_hand.cards)
        return (amount,False)
    else:
        return (amount,True)

def dealer_bust(hand,bet,amount):
    if hand.value>21:
        amount=amount+bet
        show_all(player_hand.cards,dealer_hand.cards)
        return (amount,False)
    else:
        return (amount,True)

def blackjack(hand,bet,amount):
    if hand.value==21:
        amount=amount+bet
        show_all(player_hand.cards,dealer_hand.cards)
        return (amount,False)
    else:
        return (amount,True)

def check_who_wins(player_hand,dealer_hand,bet,amount):

    if player_hand.value>dealer_hand.value:
        amount=amount+bet
        print('Player wins')
        return (amount,False)
    elif player_hand.value<dealer_hand.value:
        amount=amount-bet
        print('Dealer wins')
        return (amount,False)
    else:
        print('Its a Tie')
        return (amount,False)



amount=100

while True:

    print('WELCOME TO BLACKJACK')


    mydeck=Deck()
    mydeck.shuffle()


    # Prompt the Player for their bet
    bet=take_bet(amount)

    # Show cards (but keep one dealer card hidden)
    player_hand=Hand()
    pa=mydeck.deal()
    pb=mydeck.deal()
    player_hand.add_card(pa)
    player_hand.add_card(pb)
    player_hand.adjust_for_ace()

    dealer_hand=Hand()
    da=mydeck.deal()
    db=mydeck.deal()
    dealer_hand.add_card(da)
    dealer_hand.add_card(db)
    dealer_hand.adjust_for_ace()

    show_some(player_hand.cards,dealer_hand.cards)

    while True:

    #Player Turn
        mydeck,player_hand=player_hit_stand(mydeck,player_hand,dealer_hand)
        amount,loop=blackjack(player_hand,bet,amount)
        if loop==False:
            print('Blackjack Player wins')
            print(f'You have {amount} left in your wallet')
            break
        amount,loop=player_bust(player_hand,bet,amount)
        if loop==False:
            print('Player Busted \nDealer wins')
            print(f'You have {amount} left in your wallet')
            break


   #Dealer Turn

        mydeck,dealer_hand=dealer_hit_stand(mydeck,player_hand,dealer_hand)

        amount,loop=dealer_bust(dealer_hand,bet,amount)
        if loop==False:
            print('Dealer Busted \nPlayer wins')
            print(f'You have {amount} left in your wallet')

            break

        amount,loop=check_who_wins(player_hand,dealer_hand,bet,amount)
        if loop==False:
            print(f'You have {amount} left in your wallet')
            break
    i=input('Do you wish to play again: y or n')
    if i=='y' and amount>0:
        continue
    else:
        break
