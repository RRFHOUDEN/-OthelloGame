#othello game code
class othello_game:
    def __init__(self, width, height, boad_size):
        self.width = width
        self.height = height
        self.boad_size = boad_size
        self.boad = [["0" for _ in range(self.width)] for _ in range(self.height)]

    def can_put(self, i, j): #おけるかを調べる
        line_list = ["right", "left", False]
        col_list = ["down", "up", False]
        for line in line_list:
            for col in col_list:
                if line == False and col == False:
                    continue
                if self.can_put_direction(i, j, line, col):
                    return 1
        return False

    def can_put_direction(self, i, j, line, col):
        can = 1
        same_ij = 0
        not_same_ij = 0

        for num in range(1, self.boad_size):
            if line == "right":
                j += num
            elif line == "left":
                j -= num

            if col == "down":
                i += num
            elif col == "up":
                i -= num

            if not(0 <= i < self.boad_size and 0 <= j < self.boad_size):
                break

            if self.boad[i][j] != 0 and self.boad[i][j] != self.boad[i][j]:
                not_same_ij = 1
            elif self.boad[i][j] != 0 and self.boad[i][j] == self.boad[i][j]:
                same_ij = 1
                break
            elif self.boad[i][j] == 0:
                can = 0
        if can:
            return 1


    def update_boad(self, i, j):
        line_list = ["right", "left", False]
        col_list = ["down", "up", False]
        for line in line_list:
            for col in col_list:
                if line == False and col == False:
                    continue
                if self.can_put_direction(i, j, line, col):
                    self.update_boad_direction(i, j, line, col)

    def update_boad_direction(self, i, j, line, col):
        j_update = j
        i_update = i
        for num in range(1, self.boad_size):
            if line == "right":
                j_update += num
            elif line == "left":
                j_update -= num

            if col == "down":
                i_update += num
            elif col == "up":
                i_update -= num

            if not(0 <= i < self.boad_size and 0 <= j < self.boad_size):
                break

            if self.boad[i_update][j_update] == self.boad[i][j]:
                break
            self.boad[i_update][j_update] *= -1





