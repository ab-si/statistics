#!/bin/python3

def weighted_mean(x, w):
    '''
    Formula for weighted mean
    wm = sum(multiply(x, w)) / sum(w)
    where w denoted weight array
    '''
    mul = [a*b for a,b in zip(x, w)]
    return sum(mul)/sum(w)

if __name__ == '__main__':
    '''
    Given the two array of integers, print the weighted mean
    '''
    n = int(input())
    x, w = list(map(int, input().split())), list(map(int, input().split()))
    print("{0:.1f}".format(weighted_mean(x, w)))