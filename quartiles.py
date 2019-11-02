#!/bin/python3

def find_median(ar):
    '''
    Median for odd no of inetegers: middle value of sorted array
    Median for even array: average of 2 middle values
    '''
    n = len(ar)
    if n%2 == 0:
        return int((ar[int(n/2)] + ar[int((n-1)/2)]) / 2)
    else:
        return int(ar[int(n/2)])

if __name__ == '__main__':
    '''
    Given the array of integers, print 1st, 2nd, and 3rd quartile
    '''
    data = list(map(int, input().split()))
    data.sort()
    print(find_median(data[:n//2]))
    print(find_median(data))
    if n%2 == 0:
        print(find_median(data[(n//2):]))
    else:
        print(find_median(data[(n//2) + 1:]))
    
