# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 10:45:12 2022

@author: 44780
"""
# =============================================================================
# 
# Exercise 18.2. Write a Deck method called deal_hands that takes two parameters, the number of
# hands and the number of cards per hand. It should create the appropriate number of Hand objects,
# deal the appropriate number of cards per hand, and return a list of Hands.
# Exercise 18.3. The following are the possible hands in poker, in increasing order of value and
# decreasing order of probability:
# pair: two cards with the same rank
# two pair: two pairs of cards with the same rank
# three of a kind: three cards with the same rank
# straight: five cards with ranks in sequence (aces can be high or low, so Ace-2-3-4-5 is a straight
# and so is 10-Jack-Queen-King-Ace, but Queen-King-Ace-2-3 is not.)
# flush: five cards with the same suit
# full house: three cards with one rank, two cards with another
# 182 Chapter 18. Inheritance
# four of a kind: four cards with the same rank
# straight flush: five cards in sequence (as defined above) and with the same suit
# The goal of these exercises is to estimate the probability of drawing these various hands.
# 1. Download the following files from http: // thinkpython2. com/ code :
# Card.py : A complete version of the Card, Deck and Hand classes in this chapter.
# PokerHand.py : An incomplete implementation of a class that represents a poker hand, and
# some code that tests it.
# 2. If you run PokerHand.py, it deals seven 7-card poker hands and checks to see if any of them
# contains a flush. Read this code carefully before you go on.
# 3. Add methods to PokerHand.py named has_pair, has_twopair, etc. that return True or
# False according to whether or not the hand meets the relevant criteria. Your code should
# work correctly for “hands” that contain any number of cards (although 5 and 7 are the most
# common sizes).
# 4. Write a method named classify that figures out the highest-value classification for a hand
# and sets the label attribute accordingly. For example, a 7-card hand might contain a flush
# and a pair; it should be labeled “flush”.
# 5. When you are convinced that your classification methods are working, the next step is to estimate the probabilities of the various hands. Write a function in PokerHand.py that shuffles
# a deck of cards, divides it into hands, classifies the hands, and counts the number of times
# various classifications appear.
# 6. Print a table of the classifications and their probabilities. Run your program with larger and
# larger numbers of hands until the output values converge to a reasonable degree of accuracy. Compare your results to the values at http: // en. wikipedia. org/ wiki/ Hand_
# rankings .
# 
# =============================================================================

import random
class Card:
    """Represents a standard playing card."""
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    "represents a collection of cards"
    def __init__(self):
        'defaults to a 52 card deck with no jokers'
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)                
    def __str__(self):
        'prints a string with each card on its own line'
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def deal_a_hand(self,cards_in_hand):
        "returns a hand obect with the specified number of cards taken out of the deck"
        hand=Hand()
        for i in range(cards_in_hand):
            hand.add_card(self.pop_card())
        return hand
    
    def deal_hands(self,cards_in_hand,hands):
        'returns a list of hand objects'
        all_hands=[]
        for i in range(hands):
            all_hands.append(self.deal_a_hand(cards_in_hand))
        return all_hands
    
    def pop_card(self):
        'returns the last card object from the deck and removes that card from the deck'
        return self.cards.pop()
    
    def add_card(self, card):
        "returns a deck with an extra card"
        self.cards.append(card)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def sort(self):
        self.cards.sort()
        
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())

    class Hand(Deck):
        "represents a hand of cards - labeled by the holder"
            
        def __init__(self,label=''):
            self.cards=[]
            self.label=label
                
            def __str__(self):
                output='The cards in hand '+label+'are:\n '
                for card in self.cards:
                    output+= '%s of %s, \n' % (Card.rank_names[card.rank],
                                               Card.suit_names[card.suit])
                    return output

def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty
        
deck=Deck()
card=Card()
hand=Hand()
print(card)
hand.add_card(card)
hand.add_card(card)
hand.add_card(card)
print(hand)

