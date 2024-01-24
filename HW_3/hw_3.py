class Board_ttt:

    def __init__(self) -> None:
        self.board = [i for i in range(1, 10)]
        self.sign_x = 'X'
        self.sign_y = '0'
        self.x = 16
        self.y = -16
        self.game_over = False

    def board_to_console(self):
        b_to_c = []
        for i in range(9):
            if self.board[i] == self.x:
                b_to_c.append(self.sign_x)
            elif self.board[i] == self.y:
                b_to_c.append(self.sign_y)
            else:
                b_to_c.append(self.board[i])

        print('-'*13)
        for j in range(0,9,3):
            print(f'| {b_to_c[j]} | {b_to_c[j+1]} | {b_to_c[j+2]} |\n{"-" * 13}')

    def win_check(self, sign_user):
        if sum(self.board) == self.sign_x:
            self.game_over = True
            print("Drawn game! ")
        elif abs(sum(self.board[:3])) == 48 or abs(sum(self.board[3:6])) == 48 or abs(sum(self.board[6:10])) == 48 \
            or abs(sum(self.board[:9:3])) == 48 or abs(sum(self.board[1:9:3])) == 48 \
                or abs(sum(self.board[2:9:3])) == 48 \
                or abs(sum(self.board[0:9:4])) == 48 or abs(sum(self.board[2:7:2])) == 48:
            self.game_over = True
            print(f'User "{sign_user}" Win! ')

    def user_move(self, user_sign):
        move_cell = 3.14
        u_s = 0
        while abs(u_s) != self.x:
            try:
                move_cell = int(input(f'Enter free position number (from 1 to 9) for "{user_sign}" :\n'))
                if move_cell not in  self.board or move_cell == self.x or move_cell == self.y:
                    print('It is not a valid position number')
                    continue
                if user_sign == 'X':
                    u_s = self.x
                    self.board[move_cell-1] = u_s
                else:
                    u_s = self.y
                    self.board[move_cell-1] = u_s
            except:
                print('It is not a number')
                continue
        self.board_to_console()
        self.win_check(user_sign)

    def game_tt(self):
        while not self.game_over:
            for k in range(1, 9, 2):
                self.user_move(self.sign_x)
                if self.game_over:
                    break
                self.user_move(self.sign_y)
                if self.game_over:
                    break


if __name__ == '__main__':
    while True:
        b = Board_ttt()
        b.board_to_console()
        b.game_tt()
        y_or_no = input("Do You want to play again [Y/N]  ?: \n")
        if y_or_no.lower() == 'y':
            continue
        else:
            exit()

