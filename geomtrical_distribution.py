#!/bin/python3

'''
Problem statement:
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the 5th inspection?

geometric distribution = g(n, p) = q^(n-1)*p
p = probability of success
q = probability of failure
n = number of trials
'''
def geom(num, den, n):
    return ((1 - (num/den))**(n-1))*(num/den)

num, den = list(map(float, input().strip().split(" ")))
n = float(input())
res = geom(num, den, n)
print("{0:.3f}".format(res))