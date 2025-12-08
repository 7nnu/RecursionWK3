class Sudoku:
    def __init__(self, board):
        self.board = board
        self.size = 9
        self.stack = []
    
    def is_valid(self,row,col,num):
        # Check if num is not in the given row
        for x in range(self.size):
            if self.board[row][x] == num:
                return False

        # Check if num is not in the given column
        for x in range(self.size):
            if self.board[x][col] == num:
                return False

        # Check if num is not in the 3x3 sub-grid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False
        return True
    
    def find_next_empty(self,row,col):
        for x in range(row, self.size):
            for y in range(col if x == row else 0, self.size):
                if self.board[x][y] == 0:
                    return x, y
        return None, None
    
    def solve(self):
        if not self.stack:
            row, col = self.find_next_empty(0, 0)
            if row is not None:
                self.stack.append((row, col, 1))
            else:
                return True  # Puzzle solved
        while self.stack:
            row, col, num = self.stack.pop()
            if num > self.size:
                self.board[row][col] = 0
                continue
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                next_row, next_col = self.find_next_empty(row, col)
                if next_row is not None:
                    self.stack.append((row, col, num + 1))
                    self.stack.append((next_row, next_col, 1))
                else:
                    return True  # Puzzle solved
            else:
                self.stack.append((row, col, num + 1))
        return False
    
    def print_board(self):
        for row in self.board:
            print(" ".join(str(num) if num != 0 else '.' for num in row))
        print()
    

test_puzzle = [
[1, 0, 7, 5, 0, 0, 0, 0, 8], [0, 5, 0, 0, 0, 0, 7, 0, 0], [0, 0, 0, 0, 0, 1, 5, 6, 0], [0, 9, 3, 8, 1, 0, 0, 0, 0], [5, 0, 0, 4, 0, 7, 0, 0, 2], [0, 0, 0, 0, 2, 6, 9, 1, 0], [0, 1, 4, 2, 0, 0, 0, 0, 0], [0, 0, 9, 0, 0, 0, 0, 5, 0], [6, 0, 0, 0, 0, 4, 8, 0, 9]
]
solver = Sudoku(test_puzzle)
print("Initial Board:")
solver.print_board()
if solver.solve():
    print("Solved Board:")
    solver.print_board()
else:
    print("No solution exists.")

            
