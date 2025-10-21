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
        return "This grid consists of " + str(len(self.pieces)) + " pieces across " + str(self.rowLimit) + " rows and " + str(self.colLimit) + " columns"

    def pieceNames(self):
        print("Pieces in this grid:")
        for p in self.pieces:
            print(p)

    def pieceOverlapping(self, r, c) -> bool:
        for p in self.pieces:
            if(r == p.rowPos and c == p.colPos):
                return True
        return False
        
    
# print("Piece " + Piece.name + " moves " + Movement.distance + "spaces " + direction)
        
def slidingBlock(filename):
    # 4  4
    # text = "3  1  2  1  b"
    # # 1  1  1  1  b

    # details = text.split()
    # # details2 = ['3', '2', '1', '1', 'h']
    # # details3 = ['3', '2', '1', '1', 'h']

    # testPiece = Piece('Z', int(details[0]), int(details[1]), int(details[2]),
    #       int(details[3]), details[4])
    # blankPiece = Piece()
    
    # # print(testPiece)
    # # print(blankPiece)

    # testGrid = Grid(4, 4)
    # testGrid.pieces = [testPiece, blankPiece]
    # print(testGrid)
    # print(testGrid.pieceNames())
    # print(testGrid.pieceOverlapping(3, 1))
    # print(testGrid.pieceOverlapping(10, 1))
    # print(testGrid.pieceOverlapping(0, 0))
    # print(testGrid.pieceOverlapping(0, 4))


    # # Piece name can be checked
    # if(testPiece.name == 'Z'):
    #     print("ROCK THE DRAGON")

    print ("Sliding Block Puzzle Solver")
    print ("using data in file:", filename)

    # Logic for inserting pieces into the grid from file input

    # Intializing puzzle grid and each piece before its inserted
    myGrid = Grid()
    myPiece = Piece()

    # Reading in each line in file
    details2 = ["5  5", "3  1  2  1  b", "4  3  1  1  b", "1  1  2  1  b", "3  1  2  1  b",
                "0  1  2  1  b", "-1  -83  2  1  b", "0  7  2  1  b"]
    for item in details2:
        gameInput = item.split()
        if len(gameInput) == 2:
            if(int(gameInput[0]) <= 0):
                print("Error: Number of rows must be greater than zero")
                return
            elif(int(gameInput[1]) <= 0):
                print("Error: Number of columns must be greater than zero")
                return
            else:
                myGrid.rowLimit = int(gameInput[0])
                myGrid.colLimit = int(gameInput[1])
        else:

            if(int(gameInput[0]) > myGrid.rowLimit or int(gameInput[1]) > myGrid.colLimit
               or int(gameInput[0]) <= 0 or int(gameInput[1]) <= 0):
                # Handle piece falling outside of grid
                print("Warning: Piece with starting position of R,C falls outside of grid")

            elif( myGrid.pieceOverlapping(int(gameInput[0]), int(gameInput[1])) == True ):
                # Piece overlaps with a created piece 
                print("Warning: Piece with starting position of R,C overlaps with other piece")

            else:
                # Average case: Add this piece to the Grid
                myPiece = Piece('Z', int(gameInput[0]), int(gameInput[1]), int(gameInput[2]), 
                                int(gameInput[3]), gameInput[4])
                myGrid.pieces.append(myPiece)

            # elif():
            #     # Handle invalid direction of movement
            #     print("Warning: Piece with starting position of R,C has invalid movement")
    print(myGrid)
    print(myGrid.pieceNames())

    pass


slidingBlock ("proj3a.data")
    

