#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:49:37 2019

@author: guillaume
"""
import numpy as np
import random


class Board:
    
    def __init__(self, state=[]):
        
        self.score = 0
        self.play = True
        self.listmoves = []
        
        tst = np.shape(state)
        if tst == (4,4):
            self.board = state
        else:
            self.board = np.zeros((4,4), dtype=int)
    
    def __str__(self):
        string = '\n'.join([' '.join([str(self.board[i][j]) for j in range(4)]) for i in range(4)])
        return(string)
    
    def generation(self):
    
        # We choose a random position that is not use on the board
        pos = (random.randint(0,3), random.randint(0,3))
    
        while self.board[pos] != 0:
            pos = (random.randint(0,3), random.randint(0,3))
    
        # Then fill it with 2 or 4
        self.board[pos] = random.choice([2,4])
        
        self.possiblemoves()
    
    def possiblemoves(self):
        
        self.listmoves = []
        
        for direction in range(4):
            tmpboard = Board(np.copy(self.board))
            tmpboard.move(direction)
            
            if not(np.array_equal(self.board, tmpboard.board)):
                self.listmoves += [direction]
        
        # If no moves are possible : GameOver
        if len(self.listmoves) == 0:
            self.play = False
            
    def move(self, direction):
        # 0-Left, 1-Up, 2-Right, 3-Down
        if direction == 0 : 
            self.fusion_left()
        elif direction == 1 :
            self.fusion_up()
        elif direction == 2 : 
            self.fusion_right()
        elif direction == 3 :
            self.fusion_down()
    
    def fusionligne(self, ligne):
        
        res = []
        fusion = False
        for i in ligne:
            if i == 0:
                continue
            elif len(res) == 0:
                res.append(i)
            elif res[-1] == i and not(fusion):
                res[-1] = 2*i
                self.score += res[-1]
                fusion = True
            else:
                res.append(i)
                fusion = False
        
        #On remplit la réponse avec des 0:
        while len(res) < 4:
            res.append(0)
            
        return(res)
        
    def fusion_left(self):
        for i in range(4):
            self.board[i, : ] = self.fusionligne(self.board[i, :])
    
    def fusion_up(self):
        for j in range(4):
            self.board[ : , j] = self.fusionligne(self.board[ : , j])
            
    def fusion_right(self):
        for i in range(4):
            self.board[i, :: -1] = self.fusionligne(self.board[i, ::-1])
    
    def fusion_down(self):
        for j in range(4):
            self.board[::-1, j] = self.fusionligne(self.board[::-1, j])
    