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
    Given the array of integers and their frequency,
    print the interquartile range

    ex: 
    val = [1,2,3,4]
    freq = [2,2,2,2]
    data = [1,1,2,2,3,3,4,4]
    find IQR for data
    '''
    val = list(map(int, input().split()))
    freq = list(map(int, input().split()))

    data = []
    for i in range(len(val)):
        data += [val[i]] * freq[i]
    data.sort()
    q1 = find_median(data[:len(data)//2])
    q2 = find_median(data)
    if len(data)%2 == 0:
        q3 = find_median(data[(len(data)//2):])
    else:
        q3 = find_median(data[(len(data)//2) + 1:])

    print("{0:.2f}".format(q3 - q1))