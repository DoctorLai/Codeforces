#!/usr/bin/env python

n, k = map(int, raw_input().split())
a = map(int, raw_input().split())

if k > n:
    print -1
else:
    a.sort()
    print a[n - k], 0
