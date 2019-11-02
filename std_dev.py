#!/bin/python3

import math

def cal_mean(x):
    return sum(x)/len(x)

def find_stddev(x, mean):
    dist = [(i - mean)**2 for i in x]
    return math.sqrt(sum(dist)/len(x))

if __name__ == '__main__':
    '''
    Given the array of integers, print standard deviation (upto 1 decimal)
    '''
    x = list(map(int, input().split()))
    meanx = cal_mean(x)
    print("{0:.1f}".format(find_stddev(x, meanx)))
    
