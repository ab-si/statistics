#!/bin/python

def fact(n):
    return 1 if n==0 else n*fact(n-1)

def combination(n, k):
    return fact(n) / (fact(k) * fact(n-k))

def binomial(n, k, p):
    return combination(n, k) * pow(p, k) * pow(1-p, n-k)

if __name__ == "__main__":
    '''
    The ratio of boys to girls for babies born in Russia is 1.09:1.
    If there is 1 child born per birth,
    what proportion of Russian families with exactly 6 children will have at least 3 boys?
    '''
    b, g = 1.09, 1
    res = round(sum([binomial(6, i, b / (b+g)) for i in range(3, 7)]), 3)
    print(res)