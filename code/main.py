#othello game code
class othello_game:
    def __init__(self, boad_size):
        self.boad_size = boad_size
        self.boad = [[0 for _ in range(self.boad_size)] for _ in range(self.boad_size)]
        self.boad[self.boad_size // 2 - 1][self.boad_size // 2 - 1] = 1
        self.boad[self.boad_size // 2][self.boad_size // 2] = 1
        self.boad[self.boad_size // 2 - 1][self.boad_size // 2] = -1
        self.boad[self.boad_size // 2][self.boad_size // 2 - 1] = -1

    def print_boad(self):
        line = 0
        print("   ", end = "")
        for i in range(self.boad_size):
            print(i,  end = "  ")
        print()
        for i in self.boad:
            print(line, end=" ")
            line += 1
            for j in i:
                if j == 0:
                    print(" - ", end ="")
                elif j == 1:
                    print(" O ", end = "")
                elif j == -1:
                    print(" X ", end = "")
            print()

    def can_put(self, i, j, target): #おけるかを調べる
        if self.boad[i][j] != 0:
            return 0
        line_list = ["right", "left", False]
        col_list = ["down", "up", False]
        for line in line_list:
            for col in col_list:
                if line == False and col == False:
                    continue
                if self.can_put_direction(i, j, line, col, target):
                    return 1
        return False

    def can_put_direction(self, i, j, line, col, target):
        same_ij = 1
        not_same_ij = 0
        for num in range(1, self.boad_size):
            if line == "right":
                j += 1
            elif line == "left":
                j -= 1

            if col == "down":
                i += 1
            elif col == "up":
                i -= 1

            if not(0 <= i < self.boad_size and 0 <= j < self.boad_size):
                break

            if self.boad[i][j] == target * -1 and same_ij:
                not_same_ij = 1
                same_ij = 0
            elif self.boad[i][j] == target and not_same_ij:
                same_ij = 1
                break
            elif self.boad[i][j] == 0:
                return 0

        if same_ij and not_same_ij:
            return 1


    def update_boad(self, i, j, target):
        line_list = ["right", "left", False]
        col_list = ["down", "up", False]
        for line in line_list:
            for col in col_list:
                if line == False and col == False:
                    continue
                if self.can_put_direction(i, j, line, col, target):
                    self.update_boad_direction(i, j, line, col, target)

    def update_boad_direction(self, i, j, line, col, target):
        j_update = j
        i_update = i
        self.boad[i][j] = target
        for num in range(1, self.boad_size):
            if line == "right":
                j_update += 1
            elif line == "left":
                j_update -= 1

            if col == "down":
                i_update += 1
            elif col == "up":
                i_update -= 1

            if not(0 <= i_update < self.boad_size and 0 <= j_update < self.boad_size):
                break

            if self.boad[i_update][j_update] == target:
                break
            self.boad[i_update][j_update] *= -1

    def exist_can_plase(self, target):
        for i in range(self.boad_size):
            for j in range(self.boad_size):
                if self.can_put(i, j, target):
                    return 1
        return 0

    def calculate_points(self):
        team_1 = 0
        team_m1 = 0
        for i in self.boad:
            for j in i:
                if j == 1:
                    team_1 += 1
                elif j == -1:
                    team_m1 += 1
        return [team_1, team_m1]

import os
os.system('cls')
print("please input size of boad")
boad_size = int(input())
game = othello_game(boad_size)
os.system('cls')
game.print_boad()

target = 1
finish = 0
while True:
    if target == 1:
        print("O turn")
    else:
        print("X turn")

    if not game.exist_can_plase(target):
        target *= -1
        if not game.exist_can_plase(target):
            print("finish!")
            finish = 1
            break
        print("there is not exist place, where you can put.")

    if finish:
        break

    i, j = map(int, input().split())
    if i == -1 and j == -1:
        break
    if game.can_put(i, j, target):

        game.update_boad(i, j, target)
        os.system('cls')
        game.print_boad()
        target *= -1

    else:
        print("you can't put this place!")

[point1, point2] = game.calculate_points()
print(f'A team is {point1} point, B team is {point2} point')