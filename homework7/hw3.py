"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from collections import Counter
from typing import List


class TicTacToeBoardError(ValueError):
    """Base exception for tic tac toe"""

    def __init__(self, message='Incorrect tic tac toe board'):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class BothVictoryError(TicTacToeBoardError):
    def __init__(self, message='Both players have winning line'):
        self.message = message


class IncorrectSymbolsError(TicTacToeBoardError):
    def __init__(self, message="Only 'x', 'o', '-' should be on board"):
        self.message = message


class TicTacToeBoard:
    def __init__(self, lines: List[List[str]]):
        self.lines = lines
        self.__check_symbols_on_board()

    def check_winner(self) -> str:
        board_result = 'draw'

        for line in self.__get_all_possible_lines():
            line_result = self.check_line(line)

            if board_result == line_result:
                continue

            if 'x' in line_result:
                if 'o' in board_result:
                    raise BothVictoryError
                board_result = 'x wins'

            elif 'o' in line_result:
                if 'x' in board_result:
                    raise BothVictoryError
                board_result = 'o wins'

            elif 'unfin' in line_result and board_result == 'draw':
                board_result = 'unfinished'

        return board_result

    @staticmethod
    def check_line(line: List[str]) -> str:
        stat = Counter(line)
        if stat['-'] > 0:
            return 'unfinished'
        if stat['x'] == 3:
            return 'x wins'
        if stat['o'] == 3:
            return 'o wins'
        return 'draw'

    def get_horizontal_line(self, number) -> List[str]:
        return self.lines[number]

    def get_vertical_line(self, number) -> List[str]:
        return [line[number] for line in self.lines]

    def get_main_diagonal(self) -> List[str]:
        return [self.lines[i][i] for i in range(3)]

    def get_side_diagonal(self) -> List[str]:
        return [self.lines[i][2 - i] for i in range(3)]

    def __get_all_possible_lines(self):
        for i in range(3):
            yield self.get_horizontal_line(i)
            yield self.get_vertical_line(i)
        yield self.get_main_diagonal()
        yield self.get_side_diagonal()

    def __get_every_element(self):
        for line in self.lines:
            for symbol in line:
                yield symbol

    def __check_symbols_on_board(self):
        for symbol in self.__get_every_element():
            if symbol not in ('x', 'o', '-'):
                raise IncorrectSymbolsError

    def __str__(self):
        return '\n'.join(map(str, self.lines))


def tic_tac_toe_checker(board: TicTacToeBoard) -> str:
    """Checks if there are some winners on tic tak toe board"""
    return board.check_winner()
