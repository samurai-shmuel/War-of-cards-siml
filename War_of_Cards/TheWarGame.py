# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 18:21:16 2020

@author: Samuel
"""
from classes import Card
from classes import Player
from classes import Deck

player1 = Player(input("Type your name, player1: "))
player2 = Player(input("Type your name, player2: "))

decker = Deck()
decker.shuffle()

for cd in range(26):
    player1.increase(decker.deal())
    player2.increase(decker.deal())
    
game_on = True
round=0
while game_on:
    round+=1
    print("Round",round)
    
    if (len(player2.allcards) > len(player1.allcards)) and round >= 10000:
        print("Rounds up!", player1.name, "loses and", player2.name, "wins")
        game_on = False
        break
    
    if (len(player1.allcards) > len(player2.allcards)) and round >= 10000:
        print("Rounds up!", player2.name, "loses and", player1.name, "wins")
        game_on = False
        break
    
    if len(player1.allcards) == 0:
        print(player1.name, "loses and", player2.name, "wins")
        game_on = False
        break
    
    if len(player2.allcards) == 0:
        print(player2.name, "loses and", player1.name, "wins")
        game_on = False
        break
    
    pl1_field = []
    pl1_field.append(player1.remove())
    
    pl2_field = []
    pl2_field.append(player2.remove())
    
    
    war = True
    while war:
        if pl1_field[-1].value > pl2_field[-1].value:
            player1.increase(pl1_field)
            player1.increase(pl2_field)
            war = False
            
        elif pl2_field[-1].value > pl1_field[-1].value:
            player2.increase(pl1_field)
            player2.increase(pl2_field)
            war = False
        
        else:
            print("War Erupts! Field your men!")
            
            if len(player1.allcards)<3:
                print(f"{player1.name} is short of warriors, hence {player2.name} wins")
                war = False
                game_on = False
                break
            
            elif len(player2.allcards)<3:
                print(f"{player2.name} is short of warriors, hence {player1.name} wins")
                war = False
                game_on = False
                break
            
            else:
                for num in range(3):
                    pl1_field.append(player1.remove())
                    pl2_field.append(player2.remove())
            
            
    