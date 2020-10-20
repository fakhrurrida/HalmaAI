class Square():
    
    #Goal constants (TILE)
    T_NONE = 0
    T_GREEN = 1
    T_RED = 2

    # Piece constants (PIECE)
    P_NONE = 0
    P_GREEN = 1
    P_RED = 2

    
    def __init__(self, tile=0, piece=0, row=0, col=0):
        self.tile = tile
        self.piece = piece

        self.row = row
        self.col = col
        self.loc = (row, col)
    
        
    def getLoc(self):
        return self.loc
    
    def setLoc(self, row, col):
        self.loc = (row, col)
        
    
    