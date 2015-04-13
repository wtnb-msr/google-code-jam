#!/usr/bin/env python

import sys

structure = dict()
MINUS = True
PLUS = False
structure['11'] = (PLUS, '1')
structure['1i'] = (PLUS, 'i')
structure['1j'] = (PLUS, 'j')
structure['1k'] = (PLUS, 'k')

structure['i1'] = (PLUS, 'i')
structure['ii'] = (MINUS, '1')
structure['ij'] = (PLUS, 'k')
structure['ik'] = (MINUS, 'j')

structure['j1'] = (PLUS, 'j')
structure['ji'] = (MINUS, 'k')
structure['jj'] = (MINUS, '1')
structure['jk'] = (PLUS, 'i')

structure['k1'] = (PLUS, 'k')
structure['ki'] = (PLUS, 'j')
structure['kj'] = (MINUS, 'i')
structure['kk'] = (MINUS, '1')

structure['-1'] = (MINUS, '1')
structure['-i'] = (MINUS, 'i')
structure['-j'] = (MINUS, 'j')
structure['-k'] = (MINUS, 'k')

structure['1-'] = (MINUS, '1')
structure['i-'] = (MINUS, 'i')
structure['j-'] = (MINUS, 'j')
structure['k-'] = (MINUS, 'k')

def reduce_chars(sign, a, b):
    s, c = structure[a + b]
    return sign ^ s, c

def left_search_with_compaction(chars, matcher):
    if len(chars) < 2:
        return False
    sign = PLUS
    for i in range(len(chars) - 1 - 2): # -2 for 'j', 'k'
        left = chars.pop(0)
        right = chars.pop(0)
        print 'sign', sign, ', left', left, 'right', right
        sign, char = reduce_chars( sign, left, right )
        chars.insert(0, char)
        print 'sign', sign, ', char', char
        if sign == PLUS and char == matcher:
            return True
    return False


def right_search_with_compaction(chars, matcher):
    if len(chars) < 2:
        return False
    sign = PLUS
    for i in range(len(chars) - 1 - 2): # -2 for 'i', 'j'
        right = chars.pop()
        left = chars.pop()
        print 'sign', sign, ', left', left, 'right', right
        sign, char = reduce_chars( sign, left, right )
        chars.append(char)
        print 'sign', sign, ', char', char
        if sign == PLUS and char == matcher:
            return True
    return False


def left_search(start, chars, match, skip_count):
    sign = PLUS
    char = chars[start]
    if char == match:
        if skip_count > 0:
            skip_count -= 1
        else:
            return start
    for i in range(start + 1, len(chars)):
        #print 'sign', sign, ', left', char, 'right', chars[i]
        sign, char = reduce_chars( sign, char, chars[i] )
        #print 'sign', sign, ', char', char
        if sign == PLUS and char == match:
            if skip_count > 0:
                skip_count -= 1
            else:
                return i
    return -1

def left_search_indices(chars, left_index, right_index, matcher, period = None, targets = list()):
    sign = PLUS
    indices = list()
    char = chars[left_index]
    if sign is PLUS and char is matcher:
        if left_index + 1 in targets:
            return True
        indices.append(left_index)
    for i in range(left_index + 1, right_index + 1):
        if period is not None and i > left_index + 1 + period:
            break
        left, right = char, chars[i]
        #print 'sign', sign, ', left', left, 'right', right
        sign, char = reduce_chars( sign, left, right )
        #print 'sign', sign, ', char', char
        if sign is PLUS and char is matcher:
            if i + 1 in targets:
                return True
            indices.append(i)
    return indices if len(targets) == 0 else False

def right_search_indices(chars, left_index, right_index, matcher, period = None):
    sign = PLUS
    indices = list()
    char = chars[right_index]
    if sign is PLUS and char is matcher:
        indices.append(right_index)
    for i in range(right_index - 1, left_index - 1, -1):
        if period is not None and i < right_index - 1 - period:
            break
        left, right = chars[i], char
        #print 'sign', sign, ', left', left, 'right', right
        sign, char = reduce_chars( sign, left, right )
        #print 'sign', sign, ', char', char
        if sign is PLUS and char is matcher:
            indices.append(i)
    return indices


def search(chars, x):
    # chars * 4 => 1
    use_period = True if x > 4 else False
    use_period = False
    period = len(chars) * 4 if use_period else None
    length = len(chars) * x
    chars = chars * x

    i_indices = left_search_indices(chars, 0, length - 3, 'i', period)
    if len(i_indices) == 0:
        return 'NO'
    #print i_indices

    k_indices = right_search_indices(chars, 2, length - 1, 'k', period)
    if len(k_indices) == 0:
        return 'NO'
    k_indices.reverse()
    #print k_indices

    if not use_period:
        #print 'not use period'
        for i_index in i_indices:
            targets = { k for k in k_indices if k > i_index }
            is_found_j = left_search_indices(chars, i_index + 1, length - 2, 'j', period, targets)
            if is_found_j:
                return 'YES'
    else:
        #print 'use period'
        for i_index in i_indices:
            j_indices = left_search_indices(chars, i_index + 1, length - 2, 'j', period)
            for j_index in j_indices:
                for k_index in [ k for k in k_indices if k > j_index ]:
                    if (k_index - j_index - 1 % period) == 0:
                        return 'YES'

    return 'NO'
#
#            if len(j_indices) == 0:
#                continue
#            #print j_indices
#
#            if use_period:
#                for j_index in j_indices:
#                    for k_index in [ k for k in k_indices if k > j_index ]:
#                        if (k_index - j_index - 1 % period) == 0:
#                            return 'YES'
#
#            else:
#                for j_index in j_indices:
#                    for k_index in [ k for k in k_indices if k > j_index ]:
#                        if j_index + 1 == k_index:
#                            return 'YES'
#
    return 'NO'


def solve(chars, x):
    chars_x = chars * x
    length_chars_x = len(chars_x)

    if length_chars_x < 3:
        return 'NO'
    if length_chars_x == 3:
        if chars_x[0] == 'i' and chars_x[1] == 'j' and chars_x[2] == 'k':
            return 'YES'
        else:
            return 'NO'
    else:
        return search(chars, x)

       #skip_count_i = 0
        #skip_count_j = 0
        #skip_count_k = 0
        #chars = chars * x
        #print chars
        #search_count_i = 0
        #search_count_k = 0
        #while True:
        #    if search_count_i == 0 :
        #        is_found_i = chars[0] == 'i'
        #        search_count_i += 1
        #        if not is_found_i:
        #            continue
        #    else:
        #        is_found_i = left_search_with_compaction(chars, 'i')
        #        search_count_i += 1
        #        if not is_found_i:
        #            return 'NO'

        #    if is_first_k:
        #        is_found_k = chars[len(chars) - 1] == 'k'
        #        is_first_k = False
        #        if not is_found_k:
        #            continue
        #    else:
        #        is_found_k = right_search_with_compaction(chars, 'i')
        #        if not is_found_k:
        #            return 'NO'

        #    index = left_search(1, chars_for_j, 'j', skip_count_j)
        #    print 'j', index
        #    if index < 0:
        #        continue
        #    skip_count_j += 1
        #    index = left_search(index + 1, chars, 'k', skip_count_k)
        #    print 'k', index
        #    if index < 0:
        #        continue
        #    skip_count_k += 1

        #    if index == len(chars) - 1:
        #        return 'YES'
        #    else:
        #        return 'NO'

def run():
    reader = sys.stdin
    num_case = int(reader.readline().rstrip())
    for case in range(1, num_case + 1):
        l, x = map(int, reader.readline().rstrip().split(' '))
        chars = reader.readline().rstrip()
        result = solve(list(chars), x)
        print_result(case, result)


def print_result(i, result):
    print 'Case #%d: %s' % (i, result)


if __name__ == '__main__':
    run()
