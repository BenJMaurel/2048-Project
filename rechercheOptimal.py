#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:28:22 2019

@author: guillaume
"""

import BoardClassRap as b
import random 
import numpy as np
import time

import os

def rechercheOptimal(nbtrys = 100):

    board = b.Board()
    board.generation()

    while board.play:
        
        maxavg = 0
        bestdir = -1
        
        for d in board.listmoves:
            
            sumscore = 0
            
            for i in range(nbtrys):
                sumscore += randmovesfini(np.copy(board.board), d)
            
            avg = sumscore/nbtrys
            if avg > maxavg :
                maxavg = avg
                bestdir = d
        
        board.move(bestdir)
        
        os.system('clear')
        print(board)
        time.sleep(0.5)
        
        board.generation()
        
        os.system('clear')
        print(board)
        
    return(board.score, board.board)

def randmovesfini(boardinit, firstmove, nbmove=10):
    board = b.Board(boardinit)
    board.move(firstmove)
    
    board.generation()
        
    for i in range(nbmove):
        
        if board.play :
            board.move(random.choice(board.listmoves))
            board.generation()

    return(board.score)

#rechercheOptimal()