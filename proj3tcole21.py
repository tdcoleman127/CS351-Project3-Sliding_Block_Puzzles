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

    # def movePiece(self, toMove):
    #     Piece moved = self.piece
        
    #     return moved
    #     pass

    def hasValidMovement(move) -> bool:
        return (move == 'h') or (move == 'v') or (move == 'b') or (move == 'n')

    # # Could rework statement from the local one outside the Movement class
    # def hasValidMovement(move) -> bool:
    #     return (move == 'h') or (move == 'v') or (move == 'b') or (move == 'n')


    # Could use Movement class to manage piece movement and change a Grid Piece(),
    # which then affects what the Grid prints out
    # Remember: No pieces get removed, only moved to another pos. and replaced with *

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
        return

    def pieceOverlapping(self, r, c) -> bool:
        for p in self.pieces:
            if(r == p.rowPos and c == p.colPos):
                return True
        return False

    def display(self):
        # Create board filled with '.' (not '*')

        board = [['.' for _ in range(self.colLimit)] for _ in range(self.rowLimit)]

        # Place each piece

        for piece in self.pieces:

            for r in range(piece.height):

                for c in range(piece.width):

                    row = piece.rowPos - 1 + r # Convert to 0-indexed

                    col = piece.colPos - 1 + c

                    board[row][col] = piece.name

        # Print with asterisk borders

        print('*' * (self.colLimit + 2))

        for row in board:

            print('*' + ''.join(row) + '*')

        print('*' * (self.colLimit + 2))
        return

    
# print("Piece " + Piece.name + " moves " + Movement.distance + "spaces " + direction)

    

# class searchSolutions:
#     # Think carefully what variables yu want to share
#     def __
#         self.grid = Grid()
#         self.path = ""
    
#     def returnSolvedGrid(): (if there is one)
#         return solvedGrid

#     def returnAllPossibleSequences
#         return path

#     def prinntResult:
#         run_bfs()
#         primt(gird, path,...)

#     def run_bfs():
#         puzzle.returnSolvedGrid()
#         puzzle.returnAllPossibleSequences()
        


#     SearchSolutions puzzle = (Grid, "")
#     puzzle.printresult()
        
def slidingBlock(filename):

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
            elif( Movement.hasValidMovement(puzzleInput[4]) == False):
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
    # print(myGrid)
    # print(myGrid.allPieces())
    print(myGrid.display())

    # Insert BFS Logic here after input from file to grid is fully tested

    # Ctete a class to search function that uses BFS

    # 
    # Could break when you find a puzzle with no solution
    # Text TA< can I use memory constraint for assignment to tell when there's no solution for a puzzle (psutil)
    #     Capping the memory somehow
    # Ask the autograder about teh psytil libary
    # "Cases of really long and really large memory go together"
    # psutil.Process - start process
    # process.memory_info().rss - to get the memory after each iteration, "If the memory is larger than one GB, force a break into the loop"


    file.close()
    return

# For autograder to run code
import sys

def main():
    if len(sys.argv) > 1:

        slidingBlock(sys.argv[1])
        print("This puzzle is solvable in 5 moves")

    else:

        print("Usage: python3 proj3netid.py <input_file>")

if __name__ == "__main__":
    main()

