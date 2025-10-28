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
    
    def canMoveDown(self):
        return (self.moves == 'v') or (self.moves == 'b')
    
    def canMoveUp(self):
        return (self.moves == 'v') or (self.moves == 'b')
    
    def canMoveLeft(self):
        return (self.moves == 'h') or (self.moves == 'b')
    
    def canMoveRight(self):
        return (self.moves == 'h') or (self.moves == 'b')


class Movement:
    def __init__ (self, piece=None, direction="u", distance=0):
        self.piece = piece
        self.direction = direction
        self.distance = distance

    def hasValidMovement(move) -> bool:
        return (move == 'h') or (move == 'v') or (move == 'b') or (move == 'n')

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
        # Piece overlap = ("", rowPos=0, colPos=0, width=0, height=0, moves="n"):
        for p in self.pieces:
            if(r == p.rowPos and c == p.colPos):
                print("There's a piece here, at: " + p.name)
                return True
        return False
    
    def isValidPosition(self, piece, newRow, newCol):
        """Check if piece can be placed at (newRow, newCol) without conflicts"""
        # Check if piece stays within grid bounds
        if newRow < 1 or newCol < 1:
            return False
        if newRow + piece.height - 1 > self.rowLimit:
            return False
        if newCol + piece.width - 1 > self.colLimit:
            return False
        # Check for overlaps with other pieces
        for other in self.pieces:
            # Don't check piece against itself
            if other.name == piece.name:
                continue
            
            # Calculate the boundaries of both rectangles
            # piece: from (newRow, newCol) to (newRow + height - 1, newCol + width - 1)
            # other: from (other.rowPos, other.colPos) to (other.rowPos + height - 1, other.colPos + width - 1
            # Check if rectangles DON'T overlap (then negate)
            noOverlap = (
                newRow + piece.height - 1 < other.rowPos or      # piece is above other
                newRow > other.rowPos + other.height - 1 or      # piece is below other
                newCol + piece.width - 1 < other.colPos or       # piece is left of other
                newCol > other.colPos + other.width - 1          # piece is right of other
            )
            # If they DO overlap, position is invalid
            if not noOverlap:
                return False
            
        return True

    def generateMoves(self):
        moves = []
        for piece in self.pieces:
            # Try moving down
            if piece.canMoveDown():
                distance = 1
                while True:
                    newRow = piece.rowPos + distance
                    if self.isValidPosition(piece, newRow, piece.colPos):
                        # Valid move - add to list
                        move = Movement()
                        move.piece = piece.name
                        move.direction = "down"
                        move.distance = distance
                        moves.append(move)
                        distance += 1
                    else:
                        break  # Can't move further, stop trying
                    
            # ... same for other directions
            # Try moving up
            if piece.canMoveUp():
                distance = 1
                while True:
                    newRow = piece.rowPos - distance
                    if self.isValidPosition(piece, newRow, piece.colPos):
                        # Valid move - add to list
                        move = Movement()
                        move.piece = piece.name
                        move.direction = "up"
                        move.distance = distance
                        moves.append(move)
                        distance += 1
                    else:
                        break  # Can't move further, stop trying
            # Try moving right
            # Looking at colPos now
            if piece.canMoveRight():
                distance = 1
                while True:
                    newCol = piece.colPos + distance
                    if self.isValidPosition(piece, piece.rowPos, newCol):
                        # Valid move - add to list
                        move = Movement()
                        move.piece = piece.name
                        move.direction = "right"
                        move.distance = distance
                        moves.append(move)
                        distance += 1
                    else:
                        break  # Can't move further, stop trying
            # Try moving left
            if piece.canMoveLeft():
                distance = 1
                while True:
                    newCol = piece.colPos - distance
                    if self.isValidPosition(piece, piece.rowPos, newCol):
                        # Valid move - add to list
                        move = Movement()
                        move.piece = piece.name
                        move.direction = "left"
                        move.distance = distance
                        moves.append(move)
                        distance += 1
                    else:
                        break  # Can't move further, stop trying
            
        return moves
    
    def isGoalReached(self):
        for p in self.pieces:
            if(p.name == 'Z' and p.colPos == self.colLimit):
                return True
        return False

    def getStateString(self):

        board = [['.' for _ in range(self.colLimit)] for _ in range(self.rowLimit)]

        for piece in self.pieces:

            for r in range(piece.height):

                for c in range(piece.width):

                    row = piece.rowPos - 1 + r # Convert to 0-indexed

                    col = piece.colPos - 1 + c

                    board[row][col] = piece.name

        lineString = ""
        for m in board:
            lineString += ''.join(m)
        lineString = lineString.replace(".", ' ')
        return lineString
        

    def applyMove(self, move):
        distToMove = move.distance
        for p in self.pieces:
            if(move.direction == "up"):
            # To apply move up
                    distToMove = -1 * distToMove
                    gridRowPos = p.rowPos
                    calc = gridRowPos + distToMove                    
                    p.rowPos = calc
                    print("Piece " + p.name + " moves " + str(-1 * distToMove) + " space(s) up")
        
            # To apply move down
            if(move.direction == "down"):
                    gridRowPos = p.rowPos
                    calc = gridRowPos + distToMove                    
                    p.rowPos = calc
                    print("Piece " + p.name + " moves " + str(distToMove) + " space(s) down")

            # To apply move left
            if(move.direction == "left"):
                    distToMove = -1 * distToMove
                    gridColPos = p.colPos
                    calc = gridColPos + distToMove
                    p.colPos = calc
                    print("Piece " + p.name + " moves " + str(-1 * distToMove) + " space(s) left")
                 
            # To apply move right
            if(move.direction == "right"):
                    gridColPos = p.colPos
                    calc = gridColPos + distToMove
                    p.colPos = calc
                    print("Piece " + p.name + " moves " + str(distToMove) + " space(s) right")

        return


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
    
import queue

class PuzzleState:
    def __init__(self, grid=None, moveList=[]):
        self.grid = grid
        self.moveList = moveList
    
    def solvePuzzle(initialGrid):
        # puzzle.returnSolvedGrid()
        # puzzle.returnAllPossibleSequences()

        # Check if already at goal
        if initialGrid.isGoalReached():
            return []  # Already solved, 0 moves
        
        # BFS setup
        my_queue = queue.Queue()
        visited = set()

        # Add initial state
        initialState = PuzzleState(initialGrid, [])
        my_queue.put(initialState)
        visited.add(initialGrid.getStateString())

        # BFS loop
        while not my_queue.empty():
            currentState = my_queue.get()

            # Generate all possible moves
            possibleMoves = currentState.grid.generateMoves()

            for move in possibleMoves:

                # Apply move to get new grid state
                stateString = ""
                newGrid = Grid()
                newGrid = currentState.grid.applyMove(move)
                stateString = newGrid.getStateString()

                # Skip if we've seen this state before
                if stateString in visited:
                    continue

                visited.add(stateString)

                # Check if goal reached
                if newGrid.isGoalReached():
                    return currentState.moveList + [move]
                
                # Add new state to queue
                newState = PuzzleState(newGrid, currentState.moveList + [move])
                my_queue.put(newState)
                    
        # Queue is empty and we never found goal
        # This means NO SOLUTION exists
        return None        
        
def slidingBlock(filename):

    # Intializing puzzle grid and each piece before its inserted
    myGrid = Grid()
    myPiece = Piece()

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

    # print(myGrid.display())
    # print(myGrid.getStateString())
    
    result = []
    result = PuzzleState.solvePuzzle(myGrid)
    if(result == None):
        print("This puzzle has no solution")
    else:
        # Take apart result
        # Get number of steps needed to solve puzzle
        count = 0
        for m in result:
            count += 1
            print(count + ". Piece " + m.piece.name + " moves " + m.distance + " space(s) " + m.direction)
        print("This puzzle is solvable in " +  count + " moves")
    file.close()
    return

# For autograder to run code
import sys

def main():
    if len(sys.argv) > 1:

        slidingBlock(sys.argv[1])

    else:

        print("Usage: python3 proj3netid.py <input_file>")

if __name__ == "__main__":
    main()

