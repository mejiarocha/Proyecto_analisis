
class Board:
    
    def board_init():
        with open("board.txt") as file:
            size_line = file.readline().strip()
            size = tuple(map(int, size_line.split(",")))
            num_rows, num_cols = size  # Almacenar los valores de tamaño en variables diferentes
            matrix = []
            for i in range(num_rows):
                row = []
                values = file.readline().strip().split()
                for val in values:
                    row.append("{:0>{}}".format(val, len(str(num_cols))))
                matrix.append(row)
        return matrix, size
    
    def board_print(matrix):
        for row in matrix:
            print(" ".join(str(cell) for cell in row))

        
B = Board
matrix, size = B.board_init()
B.board_print(matrix)


