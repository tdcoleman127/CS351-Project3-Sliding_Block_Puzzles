# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 12:44:15 2025

@author: troy

Starter code for CS 351 F25 Project 3
 - Sliding Block Puzzles
"""
class Piece:
    def __init__ (self):
        self.name = ""      # name of piece
        self.rowPos = 0     # current row of upper left corner
        self.colPos = 0     # current column of upper left corner
        self.width = 0      # width in columns
        self.height = 0     # height in rows
        self.moves = "n"    # type of allowed movement
        
class Movement:
    def __init__ (self):
        self.piece = None
        self.direction = "u"
        self.distance = 0

class Grid:
    def __init__ (self):
        self.pieces = []    # list of all pieces
        
def slidingBlock(filename):
    print ("Sliding Block Puzzle Solver")
    print ("using data in file:", filename)
    pass


slidingBlock ("proj3a.data")
    

