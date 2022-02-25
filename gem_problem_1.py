# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")

class board:
    def __init__(self):
        self.rows = [1, 3, 5, 7]

    def remove_sticks(self, row, numRemove):
        self.rows[row] = self.rows[row] - numRemove

    def num_sticks(self, row):
        return self.rows[row]

    def has_sticks(self):
        for i in self.rows:
            if i:
                return True
        return False

    def replace_sticks(self, row, numSticks):
        self.rows[row] = numSticks

    def print_board(self):
        for rowNum in range(len(self.rows)):
            pipes = "|" * self.rows[rowNum]
            print(f"#{rowNum + 1}: {pipes}")

def remove_sticks_p1(board):
    for row in range(4):
        numSticks = board.num_sticks(row)

        if numSticks == 1:
            board.remove_sticks(row, 1)
            return 1, row

        if numSticks == 0:
            continue

        if numSticks%2 == 0:
            board.remove_sticks(row, numSticks)
            return numSticks, row

        else:
            board.remove_sticks(row, numSticks - 1)
            return numSticks - 1, row

def check_win(board):
    check = 0
    for row in range(4):
        check = board.num_sticks(row) ^ check

    return check

def check_row(board, row):
    count = 0
    currentSticks = board.num_sticks(row)
    for numRemoved in range(currentSticks):
        board.remove_sticks(row, 1)
        count += 1
        if (check_win(board) == 0):
            return count
    board.replace_sticks(row, currentSticks)
    return

def remove_sticks_p2(board):
    for row in range(4):
        count = check_row(board, row)
        if count:
            return count, row

    return remove_sticks_p1(board)


board = board()
player = 1
count = 0
while (board.has_sticks() and count < 20):
    numRemoved = 0
    row = 0
    if (player == 0):
        player = 2
        numRemoved, row = remove_sticks_p2(board)
    else:
        numRemoved, row = remove_sticks_p1(board)
    board.print_board()
    print(f"Player #{player} removed {numRemoved} sticks from row {row + 1}")
    player = (player + 1)%2
    count += 1

winner = (player + 1)%2
if (winner == 0):
    winner = 2
print(f"Player {winner} won")
