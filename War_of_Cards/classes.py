# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:15:58 2020

@author: Samuel
The Classes
"""
import random

values = {'Two':2, 'Three':3, 'Four':4, "Five":5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten': 10, 'Jack':11, 'Queen':12, 'King':13, 'Ace': 14}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Hearts', 'Clubs', 'Diamonds', 'Spades')

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value= values[rank]
    
    def __str__(self):
        print(self.rank, "of", self.suit)
        
class Deck:
    def __init__(self):
        self.allcards = []
        
        for suit in suits:
            for rank in ranks:
                self.allcards.append(Card(rank, suit))
    def shuffle(self):
        random.shuffle(self.allcards)
    
    def deal(self):
        return self.allcards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.allcards = []
        
    def remove(self):
        return self.allcards.pop(0)
    
    def increase(self, slot):
        if type(slot) == type([]): #if a batch, then add
            self.allcards.extend(slot)
        else:
            self.allcards.append(slot)
            
    def __str__(self):
        return f"Player {self.name}, owner of {len(self.allcards)} cards."
        
        
        
        
        
    

