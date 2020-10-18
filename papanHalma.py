from square import Square

class Papan():
    
    def __init__(self, b_size):
        board = [[None for i in range(b_size)] for j in range(b_size)]
        
        for row in range(b_size):
            for col in range(b_size):
                if row + col < 4:
                    element = Square(2, 2, row, col)
                elif row + col > 2 * (b_size - 3):
                    element = Square(1, 1, row, col)
                else:
                    element = Square(0, 0, row, col)

                board[row][col] = element
    
        #Kondisi Permainan
        self.computer = Square.P_RED
        self.b_size = b_size
        self.board = board
        self.t_limit = 60
        self.selected_square = None
        self.valid_moves = []
        self.current_turn = Square.P_GREEN
        self.eksekusi = False

        self.green_goals = [x for row in board for x in row if x.tile == Square.T_GREEN]
        self.red_goals = [y for row in board for y in row if y.tile == Square.T_GREEN]

    #if self.current_turn == self.computer:
    #    self.execute()
    
    #Fungsi eksekusi move computer/Red (AI)
    #def execute(self):

    def move(self, before, after):
        after.piece = before.piece
        before.piece = Square.P_NONE




