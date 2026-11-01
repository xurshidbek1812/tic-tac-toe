class Game:
    def __init__(self, player):
        if player == 'X' or player == 'x':
            self.player = 'X'
        else:
            self.player = 'O'

        self.board = [[' ' for n in range(3)] for n in range(3)]

    def DisplayBoard(self):
        print('   |   |   ')
        print(' ' + self.board[0][0] + ' | ' + self.board[0][1] + ' | ' + self.board[0][2] + ' ')
        print('___|___|___')
        print('   |   |   ')
        print(' ' + self.board[1][0] + ' | ' + self.board[1][1] + ' | ' + self.board[1][2] + ' ')
        print('___|___|___')
        print('   |   |   ')
        print(' ' + self.board[2][0] + ' | ' + self.board[2][1] + ' | ' + self.board[2][2] + ' ')
        print('   |   |   ')

    def WhoseTurn(self, board):
        countX = countO = 0

        for n in range(3):
            for m in range(3):
                if board[n][m] == 'X':
                    countX += 1
                elif board[n][m] == 'O':
                    countO += 1

        if countX + countO == 9:
            return 'over'
        elif countX > countO:
            return 'O'
        return 'X'

    def PlayerMove(self):
        print('You are: ' + self.player)
        player = int(input('Enter a move(1-9): '))
        while player < 1 or player > 9 or self.board[(player - 1)//3][(player - 1) % 3] != ' ':
            print('Invalid move!')
            player = int(input('Enter again: '))

        self.board[(player - 1)//3][(player - 1) % 3] = self.player

    def Check(self, board):
        if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] != ' ':
            if board[0][0] == 'X':
                return 1
            return -1
        if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] != ' ':
            if board[1][0] == 'X':
                return 1
            return -1
        if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] != ' ':
            if board[2][0] == 'X':
                return 1
            return -1

        if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] != ' ':
            if board[0][0] == 'X':
                return 1
            return -1
        if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] != ' ':
            if board[0][1] == 'X':
                return 1
            return -1
        if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] != ' ':
            if board[0][2] == 'X':
                return 1
            return -1

        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
            if board[0][0] == 'X':
                return 1
            return -1
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
            if board[0][2] == 'X':
                return 1
            return -1

        count = 0
        for n in range(3):
            for m in range(3):
                if board[n][m] == ' ':
                    count += 1

        if count == 0:
            return 0

        return 2


    def Evaluate(self, board):
        evaluation = self.Check(board)

        if evaluation != 2:
            return evaluation

        side = self.WhoseTurn(board)

        if side == 'X':
            evaluation = -2

        for n in range(3):
            for m in range(3):
                if board[n][m] == ' ':
                    new_board = [row.copy() for row in board]
                    new_board[n][m] = side
                    new_evaluation = self.Evaluate(new_board)

                    if side == 'X':
                        evaluation = max(evaluation, new_evaluation)
                    else:
                        evaluation = min(evaluation, new_evaluation)

        return evaluation

    def ComputerMove(self):
        side = self.WhoseTurn(self.board)

        evaluation = -2
        if side == 'O':
            evaluation = 2

        row = column = -1

        for n in range(3):
            for m in range(3):
                if self.board[n][m] == ' ':
                    new_board = [row.copy() for row in self.board]
                    new_board[n][m] = side
                    new_evaluation = self.Evaluate(new_board)

                    if side == 'X':
                        if new_evaluation == 1:
                            return [n, m]
                        elif new_evaluation == 0:
                            evaluation = 0
                            row = n
                            column = m
                        elif evaluation == -2:
                            evaluation = -1
                            row = n
                            column = m
                    else:
                        if new_evaluation == -1:
                            return [n, m]
                        elif new_evaluation == 0:
                            evaluation = 0
                            row = n
                            column = m
                        elif evaluation == 2:
                            evaluation = 1
                            row = n
                            column = m

        return [row, column]

    def Play(self):
        if self.player == 'X':
            while True:
                print()
                self.DisplayBoard()
                print()
                self.PlayerMove()
                print()
                status = self.Check(self.board)
                if status == 1:
                    self.DisplayBoard()
                    print()
                    print('YOU WON!!!')
                    print()
                    break
                elif status == 0:
                    self.DisplayBoard()
                    print()
                    print('IT IS A TIE!!!')
                    print()
                    break

                comp_move = self.ComputerMove()
                if comp_move[0] == -1:
                    self.DisplayBoard()
                    print()
                    print('IT IS A TIE!!!')
                    print()
                    break
                self.board[comp_move[0]][comp_move[1]] = 'O'
                status = self.Check(self.board)
                if status == -1:
                    self.DisplayBoard()
                    print()
                    print('YOU LOST!!!')
                    print()
                    break
                elif status == 0:
                    self.DisplayBoard()
                    print()
                    print('IT IS A TIE!!!')
                    print()
                    break
        else:
            while True:
                comp_move = self.ComputerMove()
                if comp_move[0] == -1:
                    self.DisplayBoard()
                    print()
                    print('IT IS A TIE!!!')
                    print()
                    break
                self.board[comp_move[0]][comp_move[1]] = 'X'
                status = self.Check(self.board)
                if status == 1:
                    self.DisplayBoard()
                    print()
                    print('YOU LOST!!!')
                    print()
                    break
                elif status == 0:
                    self.DisplayBoard()
                    print()
                    print('IT IS A TIE!!!')
                    print()
                    break
                
                print()
                self.DisplayBoard()
                print()
                self.PlayerMove()
                print()
                status = self.Check(self.board)
                if status == -1:
                    self.DisplayBoard()
                    print()
                    print('YOU WON!!!')
                    print()
                    break
                elif status == 0:
                    self.DisplayBoard()
                    print()
                    print('IT IS A TIE!!!')
                    print()
                    break


if __name__ == '__main__':

    print('******Welcome to out TIC-TAC-TOE game******')
    print()

    player = input('Choose a side(X-O): ')
    if player == 'X' or player == 'x':
        player = 'X'
    else:
        player = 'O'

    new_game = Game(player)

    new_game.Play()