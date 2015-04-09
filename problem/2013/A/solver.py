#!/usr/bin/env python

import sys

class Board:

    def __init__(self):
        self.board = dict()
        for x in range(4): # yoko
            for y in range(4): # tate
                self.put(x, y, '.')

    def put(self, x, y, value):
        index = x * 4 + y
        self.board[index] = value

    def get(self, x, y):
        index = x * 4 + y
        return self.board[index]

    def is_checker(self, x, y, value):
        return value == self.get(x, y)

    def print_info(self):
        for x in range(4): # yoko
            for y in range(4): # tate
                print self.get(x, y),
            print


def is_complete(board):
    for x in range(4): # rows
        for y in range(4): # columns
            if board.is_checker(x, y, '.'):
                return False
    return True


def check(board, checker):
    # yoko
    for x in range(4): # rows
        is_win = True
        for y in range(4): # columns
            is_checker = board.is_checker(x, y, checker) or board.is_checker(x, y, 'T')
            is_win = is_win and is_checker
        if is_win:
            return is_win
    # tate
    for x in range(4): # rows
        is_win = True
        for y in range(4): # columns
            is_checker = board.is_checker(y, x, checker) or board.is_checker(y, x, 'T')
            is_win = is_win and is_checker
        if is_win:
            return is_win
    # naname
    is_win = True
    for i in range(4):
        is_checker = board.is_checker(i, i, checker) or board.is_checker(i, i, 'T')
        is_win = is_win and is_checker
    if is_win:
        return is_win
    is_win = True
    for i in range(4):
        is_checker = board.is_checker(i, 3 - i, checker) or board.is_checker(i, 3 - i, 'T')
        is_win = is_win and is_checker
    if is_win:
        return is_win

    return False


def solve(board):
    is_win_x = check(board, 'X')
    is_win_o = check(board, 'O')
    is_completed = is_complete(board)

    if is_win_x and not is_win_o:
        return 'X won'
    if not is_win_x and is_win_o:
        return 'O won'

    if is_completed:
        return 'Draw'
    else:
        return 'Game has not completed'


def run():
    reader = sys.stdin
    num_case = int(reader.readline().rstrip())

    for case in range(1, num_case + 1):
        board = Board()
        for x in range(4):
            line = reader.readline().rstrip()
            for y in range(4):
                value = line[y]
                board.put(x, y, value)
        #board.print_info()
        result = solve(board)
        print_result(case, result)
        reader.readline()


def print_result(i, result):
    print 'Case #%d: %s' % (i, result)


if __name__ == '__main__':
    run()
