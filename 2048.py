#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 10:56:46 2019

@author: guillaume
"""
import BoardClassRap as b
board = b.Board()

keys = {'z':1,
           'q':0,
           's':3,
           'd':2}

# Initialisation
board.generation()

while board.play:
    
    print(board.board)
    
    direction = 'a'
    while not(direction in keys.keys()) or not(keys[direction] in board.listmoves):
        direction = input("zqsd : ")
    
    board.move(keys[direction])
    
    board.generation()

print(board.score)