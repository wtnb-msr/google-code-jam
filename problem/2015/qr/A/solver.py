#!/usr/bin/env python

import sys


def solve(line):
    token = line.split(' ')
    max_shyness = int(token[0])
    num_standings = 0
    num_addition = 0

    for level in range(0, max_shyness + 1):
        num_level = int(token[1][level])
        if num_level == 0:
            continue
        if num_standings >= level:
            num_standings += num_level
        else:
            #print level, num_level, num_standings
            num_new_addition = level - num_standings
            num_standings += num_new_addition + num_level
            num_addition += num_new_addition
            #print level, num_level, num_new_addition, num_standings, num_addition

    return num_addition


def run():
    reader = sys.stdin
    num_case = int(reader.readline().rstrip())

    for case in range(1, num_case + 1):
        line = reader.readline().rstrip()
        result = solve(line)
        print_result(case, result)


def print_result(i, result):
    print 'Case #%d: %s' % (i, result)


if __name__ == '__main__':
    run()
