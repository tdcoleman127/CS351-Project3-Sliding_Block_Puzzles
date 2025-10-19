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

    # Created toString()-like method for Piece
    def __str__(self):
        canMove = ""
        if(self.moves == 'h'):
            canMove = "horizontal"
        elif(self.moves == 'v'):
            canMove = "vertical"
        elif(self.moves == 'b'):
            canMove = "horizontal and vertical"
        elif(self.moves == 'n'):
            canMove = "no"
        else:
            canMove = "unspecified"
        return "Piece " + self.name + " at row " + str(self.rowPos) + " and col " + str(self.colPos) + " with width " + str(self.width) + " and height " + str(self.height) + " can move in " + canMove + " directions"
        
class Movement:
    def __init__ (self):
        self.piece = None
        self.direction = "u"
        self.distance = 0

class Grid:
    def __init__ (self, rowLimit=0, colLimit=0):
        self.pieces = []    # list of all pieces
        self.rowLimit = rowLimit
        self.colLimit = colLimit

    def __str__(self):
        return "This grid consists of " + str(len(self.pieces)) + " across " + self.rowLimit + "rows and " + self.colLimit + "columns"

    def pieceNames(self):
        pass
    
# print("Piece " + Piece.name + " moves " + Movement.distance + "spaces " + direction)
        
def slidingBlock(filename):
    # 4  4
    text = "3  1  2  1  b"
    # 1  1  1  1  b

    details = text.split()
    # details2 = ['3', '2', '1', '1', 'h']
    # details3 = ['3', '2', '1', '1', 'h']

    myPiece = Piece('Z', int(details[0]), int(details[1]), int(details[2]),
          int(details[3]), details[4])
    piece2 = Piece()
    
    print(myPiece)
    print(piece2)

    # Piece name can be checked
    if(myPiece.name == 'Z'):
        print("ROCK THE DRAGON")

    print ("Sliding Block Puzzle Solver")
    print ("using data in file:", filename)

    # Logic for inserting pieces into the grid from file input
    myGrid = None
    myPiece = None
    for line in file:
        details = line.split()
        if len(details) == 2:
            myGrid = Grid(details[0], details[1])
            print("Error: Number of rows must be greater than zero")
            print("Error: Number of columns must be greater than zero")
        else:

            if(details[0] > myGrid.rowLimit or details[1] > myGrid.colLimit):
                # Handle piece falling outside of grid
                print("Warning: Piece with starting position of R,C falls outside of grid")
            myPiece = Piece('Z', int(details[0]), int(details[1]), int(details[2]),
          int(details[3]), details[4])
            # Add this piece to the Grid
            Grid.pieces.append(myPiece)
    pass


slidingBlock ("proj3a.data")
    

