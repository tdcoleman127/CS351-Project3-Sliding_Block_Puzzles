# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 12:44:15 2025

@author: troy

Starter code for CS 351 F25 Project 3
 - Sliding Block Puzzles
"""

import numpy as np

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

    # Could use Movement class to manage piece movement and restructuring of Grid pieces
    # Remember: No pieces get removed, only moved out and replaced
    # Make sure to replace former locations in Grid with *

class Grid:
    def __init__ (self, rowLimit=0, colLimit=0):
        self.pieces = []    # list of all pieces
        self.rowLimit = rowLimit
        self.colLimit = colLimit

    def __str__(self):
        return "The grid consists of " + str(len(self.pieces)) + " pieces across " + str(self.rowLimit) + " rows and " + str(self.colLimit) + " columns"

    def allPieces(self):
        print("Pieces in this grid:")
        for p in self.pieces:
            print(p)

    def pieceOverlapping(self, r, c) -> bool:
        for p in self.pieces:
            if(r == p.rowPos and c == p.colPos):
                return True
        return False
    
    def gridState(self):
        print("Matrix as array: no elements added")
        matrix = [['*' for _ in range(self.colLimit)] for _ in range(self.rowLimit)]

        for p in self.pieces:
            matrix[p.rowPos - 1][p.colPos - 1] = p.name
            
            # Handling width
            if(p.width > 1):
                print("Piece " + p.name + "'s width is " + str(p.width))
                originalColumn = p.colPos - 1
                left = p.colPos - 2
                right = p.colPos
                widthIter = p.width - 1
                print("Starting width is " + str(widthIter))
                while( (right < self.colLimit) and (matrix[p.rowPos - 1][right] == '*') and (widthIter > 0)):
                    matrix[p.rowPos - 1][right] = p.name
                    right = right + 1
                    widthIter = widthIter - 1
                    print("widthIter during right", str(widthIter))

                if(widthIter > 0):
                    print("Still need to do widthIter for left")
                    while( (left > 0) and (matrix[p.rowPos - 1][left] == '*') and (widthIter > 0)):
                        matrix[p.rowPos - 1][left] = p.name
                        left = left - 1
                        widthIter = widthIter - 1
                        print("widthIter during left", str(widthIter))
                print(str(widthIter))
                print("Ending width is 0 " + str(widthIter == 0))

            # Handling height
            if(p.height > 1):
                print("Piece " + p.name + "'s height is " + str(p.height))
                originalRow = p.rowPos - 1
                up = p.rowPos - 2
                down = p.rowPos
                heightIter = p.height - 1
                print("Starting height is " + str(heightIter))


                while( (down < self.rowLimit) and (matrix[down][p.colPos - 1] == '*') and (heightIter > 0)):
                    matrix[down][p.colPos - 1] = p.name
                    down = down + 1
                    heightIter = heightIter - 1
                    print("heightIter during down", str(heightIter))

                if(widthIter > 0):
                    print("Still need to do heightIter for up")
                    while( (up > 0) and (matrix[up][p.colPos - 1]) and (heightIter > 0)):
                        matrix[up][p.colPos - 1] = p.name
                        up = up - 1
                        heightIter = heightIter - 1
                        print("heightIter during up", str(heightIter))
                print(str(heightIter))
                print("Ending height is 0 " + str(heightIter == 0))

        
        # Need to format actual output in segments below
        print("Matrix as array: after adding elements")
        print(matrix)
        finishString = ""
        for m in matrix:
            finishString += ''.join(m) + "\n"
        print(finishString)

    
def hasValidMovement(m) -> bool:
    return (m == 'h') or (m == 'v') or (m == 'b') or (m == 'n')
    
# print("Piece " + Piece.name + " moves " + Movement.distance + "spaces " + direction)
        
def slidingBlock(filename):
    # 4  4
    text = "3  1  2  1  b"
    # # 1  1  1  1  b

    details = text.split()
    # details2 = ['3', '2', '1', '1', 'h']
    # details3 = ['3', '2', '1', '1', 'h']

    testPiece = Piece('Z', int(details[0]), int(details[1]), int(details[2]),
          int(details[3]), details[4])
    blankPiece = Piece()
    # print(hasValidMovement(details[4]))
    
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

    print ("Sliding Block Puzzle Solver")
    print ("using data in file:", filename)

    # Opening file
    if not filename:
        print("Empty filename.")
        return False
    try:
        file = open(filename, 'r')
    except (FileNotFoundError, IOError):
        print("Error occurred opening file")
        return False
    
    # Logic for inserting pieces into the grid from file input

    # Intializing puzzle grid and each piece before its inserted
    myGrid = Grid()
    myPiece = Piece()

    # details2 = ["5  5", "3  1  2  1  b", "4  3  1  1  b", "1  1  2  1  b", "3  1  2  1  b",
    #             "0  1  2  1  b", "-1  -83  2  1  b", "0  7  2  1  b", "5  5  2  1  k"]

    # Initializing variables for later use
    nameIter = 0
    possibleNames = "Z 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y"
    possibleNames = possibleNames.split()


    # Reading in each line in file
    for item in file:
        puzzleInput = item.split()
        if len(puzzleInput) == 2:
            # Checking that input rows and columns are positive integers
            if(int(puzzleInput[0]) <= 0):
                print("Error: Number of rows must be greater than zero")
                return
            elif(int(puzzleInput[1]) <= 0):
                print("Error: Number of columns must be greater than zero")
                return
            else:
                # Initializing Grid with them if they're valid
                myGrid.rowLimit = int(puzzleInput[0])
                myGrid.colLimit = int(puzzleInput[1])
        else:
            if(int(puzzleInput[0]) > myGrid.rowLimit or int(puzzleInput[1]) > myGrid.colLimit
               or int(puzzleInput[0]) <= 0 or int(puzzleInput[1]) <= 0):
                # Handle piece falling outside of grid
                print("Warning: Piece with starting position of R,C falls outside of grid")
            elif( myGrid.pieceOverlapping(int(puzzleInput[0]), int(puzzleInput[1])) == True ):
                # Piece overlaps with a created piece 
                print("Warning: Piece with starting position of R,C overlaps with other piece")
            elif( hasValidMovement(puzzleInput[4]) == False):
                # Handle invalid direction of movement
                print("Warning: Piece with starting position of R,C has invalid movement")
            else:
                # Average case: Add this piece to the Grid
                if(nameIter > 61):
                    print("Warning: Piece limit reached - 61")
                else:
                    myPiece = Piece(possibleNames[nameIter], int(puzzleInput[0]), int(puzzleInput[1]), int(puzzleInput[2]), 
                                int(puzzleInput[3]), puzzleInput[4])                
                    myGrid.pieces.append(myPiece)
                    nameIter = nameIter + 1

    # Print grid results and names of all pieces
    print(myGrid)
    print(myGrid.allPieces())
    print(myGrid.gridState())

    # Insert BFS Logic here after input from file to grid is fully tested

    file.close()


slidingBlock ("proj3f.txt")
# slidingBlock ("proj3b.txt")
# slidingBlock ("proj3k.txt")
# slidingBlock ("proj3a.data")
    

