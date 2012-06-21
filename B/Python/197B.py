#!/usr/bin/env python

from sys import stdin

n, m = map(int, stdin.readline().split(" "))

a = map(int, stdin.readline().split(" "))
b = map(int, stdin.readline().split(" "))

def gcd(a, b):
    while b != 0:
        t = a % b
        a = b
        b = t
    return a

if n > m:
    if a[0] * b[0] > 0:
        print "Infinity"
    else:
        print "-Infinity"
elif n == m:
    t = gcd(a[0], b[0])
    print "%d/%d" % (a[0] / t, b[0] / t)
else:
    print "0/1"
