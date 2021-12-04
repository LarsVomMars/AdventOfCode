LINES = [line.strip() for line in open("input").read().split("\n\n")]

BOARD_HEIGHT = 5
BOARD_WIDTH = 5


class Board:
    def __init__(self, board: str) -> None:
        self.board = self.__get_board(board)
        self.marked = [False, ] * 25

    def __get_board(self, board: str) -> list:
        return [int(val) for row in board.splitlines() for val in row.split()]

    def __get_indices(self, num: int) -> list:
        return [i for i, val in enumerate(self.board) if val == num]

    def __check_win(self) -> bool:
        return any(
            all(self.marked[i:i + BOARD_WIDTH]) for i in range(0, BOARD_WIDTH * BOARD_HEIGHT - BOARD_WIDTH, BOARD_WIDTH)
        ) or any(
            all([self.marked[j * 5 + i] for j in range(BOARD_HEIGHT)]) for i in range(BOARD_WIDTH)
        )

    def mark(self, num: int) -> bool:
        idxs = self.__get_indices(num)
        for idx in idxs:
            self.marked[idx] = True

        return self.__check_win()

    def get_unmarked_val(self) -> int:
        return sum([val for i, val in enumerate(self.board) if not self.marked[i]])


DRAWS = list(map(int, LINES[0].split(",")))
BOARDS = [Board(line) for line in LINES[1:]]


def p1():
    boards = BOARDS.copy()
    for draw in DRAWS:
        for board in boards:
            if board.mark(draw):
                return draw * board.get_unmarked_val()


def p2():
    boards = BOARDS.copy()
    removed_boards = []
    for draw in DRAWS:
        for board in boards:
            if board.mark(draw):
                removed_boards.append(board)
                if len(boards) - len(removed_boards) == 0:
                    return draw * boards[0].get_unmarked_val()

        for board in removed_boards:
            boards.remove(board)
        removed_boards = []


print("1:", p1())
print("2:", p2())
