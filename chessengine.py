"""
    This is responsible for storing the information about the current state of a game. It will
    also be responsible for determining the valid moves at the current state, it'll keep a move log
"""

class Gamestate:
    def __init__(self):
        #the board is an 8X8 2d list, each has 2 characters
        # the first character reps the color of the piece 'b' or 'w'
        # the second character reps the type of the piece 'k', 'q', 'r', 'b', 'N', or 'p'
        # '--' represents empty space with no piece.
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]

        self.whiteToMove = True
        self.moveLog = []

    # This will not work for castling


    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # log the move
        self.whiteToMove = not self.whiteToMove

    def undoMove(self):
        # undo the move, get the last move from the move log
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            print(move)
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove



    def getValidMoves(self):
        return self.getAllPossibleMoves()


    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)): # number of rows
            for c in range(len(self.board[r])): # number of columns in given row
                turn = self.board[r][c][0] # first character on the board
                if (turn == "w" and self.whiteToMove) and (turn == "b" and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == "p":
                        self.getPawnMoves(r, c, moves)
                    elif piece == "R":
                        self.getRookMoves(r, c, moves)
        return moves
    """
        Get all the pawn moves for the pawn located at row, col and add these moves to the list
    """
    def getPawnMoves(self, row, col, moves):
        pass

    def getRookMoves(self, row, col, moves):
        pass

    def getMoves(self, row, col, moves):
        pass

    def getPawnMoves(self, row, col, moves):
        pass

    def getPawnMoves(self, row, col, moves):
        pass

class Move:
    ranks_to_rows = {
        "1": 7, "2": 6 , "3": 5 , "4": 4 , "5": 3,
        "6": 2, "7": 1, "8": 0,
    }
    rows_to_ranks = {v:k for k, v in ranks_to_rows.items()}
    files_to_col = {
        "a": 0, "b": 1 , "c": 2 , "d": 3 , "e": 4,
        "f": 5, "g": 6, "h": 7,
    }
    cols_to_files = {v:k for k, v in files_to_col.items()}

    def __init__(self, startSq, endSq, board)-> None:
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID

    def get_chess_notations(self):
        return self.get_rank_files(self.startRow, self.startCol) + self.get_rank_files(self.endRow, self.endCol)


    def get_rank_files(self, r, c):
        return self.cols_to_files[c] + self.rows_to_ranks[r]

