#othello game code
import os
import readchar
import sys
import copy

class othello_game:
    def __init__(self, boad_size):
        self.boad_size = boad_size
        self.boad = [[0 for _ in range(self.boad_size)] for _ in range(self.boad_size)]
        self.boad[self.boad_size // 2 - 1][self.boad_size // 2 - 1] = 1
        self.boad[self.boad_size // 2][self.boad_size // 2] = 1
        self.boad[self.boad_size // 2 - 1][self.boad_size // 2] = -1
        self.boad[self.boad_size // 2][self.boad_size // 2 - 1] = -1

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

class controller():
    def __init__(self, boad, boad_size):
        self.boad = boad
        self.boad_size = boad_size

    def print_boad(self, i_now=-1, j_now=-1, target=0):
        for i in range(self.boad_size):
            for j in range(self.boad_size):
                if i == i_now and j == j_now:
                    if target == 1:
                        print("_O_", end = "")
                    else:
                        print("_X_", end="")

                elif self.boad[i][j] == 0:
                    print(" - ", end = "")
                elif self.boad[i][j] == 1:
                    print(" O ", end = "")
                elif self.boad[i][j] == -1:
                    print(" X ", end = "")
            print()

    def select_square(self, target, i=0, j=0):
        os.system('cls')
        if target == 1:
            print("O turn")
        else:
            print("X turn")
        self.print_boad(i, j, target)
        while True:
            input_key = readchar.readkey()
            if input_key == " ":
                return [i, j]
            if not("0" <= input_key <= "9"):
                continue
            input_num = int(input_key)
            if input_num == 9:
                input_key = input("finish?(y/n)")
                if input_key == "y":
                    return -1, -1
                else:
                    continue

            if input_num == 6:
                j += 1
            if input_num == 4:
                j -= 1
            if input_num == 2:
                i += 1
            if input_num == 8:
                i -= 1

            if i < 0:
                i = 0
            if self.boad_size <= i:
                i = self.boad_size - 1
            if j < 0:
                j = 0
            if self.boad_size <= j:
                j = self.boad_size - 1
            # sys.stdout.write(read)
            os.system('cls')
            if target == 1:
                print("O turn")
            else:
                print("X turn")
            self.print_boad(i, j, target)

class CPU_match(othello_game):
    def decide_squere(self):
        target = -1
        ij_list = []
        for i in range(self.boad_size):
            for j in range(self.boad_size):
                if self.can_put(i, j, target):
                    return i, j



def main(cpu=0):
    os.system('cls')
    print("please input size of boad")
    boad_size = int(input())
    game = CPU_match(boad_size)
    controll = controller(game.boad, game.boad_size)
    target = 1
    finish = 0
    i = 0
    j = 0

    while True:
        if not game.exist_can_plase(target):
            target *= -1
            if not game.exist_can_plase(target):
                print("finish!")
                finish = 1
                break

        if finish:
            break
        if cpu and target == -1:
            i, j = game.decide_squere()
            game.update_boad(i, j, target)
            target *= -1
            i = 0
            j = 0
            continue

        i, j = controll.select_square(target, i, j)
        if i == -1 and j == -1:
            break
        if game.can_put(i, j, target):
            game.update_boad(i, j, target)
            os.system('cls')
            controll.print_boad()
            target *= -1
            i = 0
            j = 0
    print(game.calculate_points())


if __name__ == '__main__':
    yn = input("Do you play?(y/n)")
    while yn == "y":
        cpu = input("CPU or manual or NetWork?(c/m/n)")
        if cpu == "c":
            main(1)
        elif cpu == "m":
            main()
        else:
            main(2)
        yn = input("Do you play again?(y/n)")
