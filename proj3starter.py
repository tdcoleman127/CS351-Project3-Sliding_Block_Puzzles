# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 12:44:15 2025

@author: troy

Starter code for CS 351 F25 Project 3
 - Sliding Block Puzzles
"""
class Piece:
    def __init__ (self, name="", rowPos=0, colPos=0, width=0, height=0, moves="n"):
        self.name = name     # name of piece
        self.rowPos = rowPos     # current row of upper left corner
        self.colPos = colPos     # current column of upper left corner
        self.width = width      # width in columns
        self.height = height     # height in rows
        self.moves = moves    # type of allowed movement

    def pieceDetails(self):
        print("Piece " + self.name +
              " at row " + str(self.rowPos) + " and col " + str(self.colPos)
              + " with width " + str(self.width) + " and height " + str(self.height))
        
class Movement:
    def __init__ (self):
        self.piece = None
        self.direction = "u"
        self.distance = 0

class Grid:
    def __init__ (self):
        self.pieces = []    # list of all pieces


# print("Piece " + Piece.name + " moves " + Movement.distance + "spaces " + direction)
        
def slidingBlock(filename):

    details = ['3', '2', '1', '1', 'd']

    myPiece = Piece('Z', int(details[0]), int(details[1]), int(details[2]),
          int(details[3]), details[4])
    piece2 = Piece()
    
    print(myPiece.pieceDetails())
    print(piece2.pieceDetails())


    print ("Sliding Block Puzzle Solver")
    print ("using data in file:", filename)
    pass


slidingBlock ("proj3a.data")
    

