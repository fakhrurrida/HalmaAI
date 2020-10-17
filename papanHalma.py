from square import Square

def Papan():
    
    def __init__(self, b_size):
        board = [[None for i in range(b_size)] for j in range(b_size)]
        
        for row in range(b_size):
            for col in range(b_size):
                if row + col < 4:
                    element = Square(2, 2, 0, row, col)
                elif row + col > 2 * (b_size - 3):
                    element = Square(1, 1, 0, row, col)
                else:
                    element = Square(0, 0, 0, row, col)

                board[row][col] = element
    
    
    