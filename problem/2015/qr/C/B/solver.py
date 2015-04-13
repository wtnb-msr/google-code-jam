#!/usr/bin/env python

import sys
import copy

class Plates:
    def __init__(self, plates):
        plates.sort()
        plates.reverse()
        self.plates = plates

    def insert(self, plate):
        for i, p in enumerate(self.plates):
            if plate > p:
                self.plates.insert(i, plate)
                return
        self.plates.append(plate)

    def getMax(self):
        return self.plates[0]

    def pop(self):
        return self.plates.pop(0)

    def countMore(self, plate):
        counter = 0
        for p in self.plates:
            if p > plate:
                counter += 1
            else:
                break
        return counter

    def getMore(self, plate):
        l = list()
        for p in self.plates:
            if p > plate:
                l.append(p)
            else:
                break
        return l

    def print_info(self):
        for p in self.plates:
            print p,
        print


def calc_pay(plates, num_div):
    max_plate = plates.getMax()
    div = max_plate / num_div
    if max_plate % num_div == 0:
        return max_plate - div, div
    else:
        return max_plate - (div + 1), (div + 1)



def calc_effective(plates, num_div):
    max_plate = plates.getMax()
    pay, div = calc_pay(plates, num_div)
    #cost = num_div - 1 +  plates.countMore( div ) - 1
    cost = num_div - 1
    cost *= plates.countMore( div )
    effective = pay - cost
    #if div < 3:
        ##return -1

    #print 'num_div, div, pay, divcost, more, e'
    #print num_div, div, pay, num_div - 1, plates.countMore( div ) - 1, effective
    #print 'num_div: ', num_div, ', effective: ', effective
    return effective


def calc_divide(plates):
    #print 'div1'
    effective = 0
    opt_divide = 1
    for num_div in range(2, plates.getMax()):
        e = calc_effective(plates, num_div)
        #print 'effect'
        #print num_div, e
        if e < 1:
            return opt_divide
        if e >= effective:
            effective = e
            opt_divide = num_div
            continue
        else:
            return opt_divide

def calc_divide2(plates):
    print 'div2'
    effective = 0
    opt_divide = 1
    for num_div in range(2, plates.getMax()):
        e = calc_effective(plates, num_div)
        #print 'effect'
        #print num_div, e
        if e < 1:
            return opt_divide
        if e > effective:
            effective = e
            opt_divide = num_div
            continue
        else:
            return opt_divide


def devide(max_plate, num_div):
    divs = [ max_plate / num_div ] * num_div
    for i in range(max_plate % num_div):
        divs[i] += 1
    return divs


def solve(num_diners, plates):
    plates.print_info()
    num_specials = 0
    while (plates.getMax() > 3):
        num_div = calc_divide(plates)
        if num_div > 1:
            #print 'divide:', num_div
            divs = devide(plates.getMax(), num_div)
            plates.pop()
            for div in divs:
                plates.insert(div)
            num_specials += num_div - 1
            plates.print_info()
        else:
            break

    result = num_specials + plates.getMax()
    #print 'result,  num_specials , plates.getMax()'
    #print result,  num_specials , plates.getMax()
    return result

def solve2(num_diners, plates):
    plates.print_info()
    num_specials = 0
    while (plates.getMax() > 3):
        num_div = calc_divide2(plates)
        if num_div > 1:
            #print 'divide:', num_div
            divs = devide(plates.getMax(), num_div)
            plates.pop()
            for div in divs:
                plates.insert(div)
            num_specials += num_div - 1
            plates.print_info()
        else:
            break

    result = num_specials + plates.getMax()
    #print 'result,  num_specials , plates.getMax()'
    #print result,  num_specials , plates.getMax()
    return result


def run():
    reader = sys.stdin
    num_case = int(reader.readline().rstrip())
    for case in range(1, num_case + 1):
        num_diners = int(reader.readline().rstrip())
        plates = Plates( map(int, reader.readline().rstrip().split(' ')) )
        #plates2 = copy.deepcopy(plates)
        result = solve(num_diners, plates)
        #result2 = solve2(num_diners, plates2)
        #result = result if result < result2 else result2
        plates.print_info()
        print_result(case, result)


def print_result(i, result):
    print 'Case #%d: %s' % (i, result)


if __name__ == '__main__':
    run()
