#!/usr/bin/env python

n = int(raw_input())
a = [raw_input().split(' ') for x in range(0, n)]

r = {}
b = []

for i in range(0, n):
    x, y = a[i]
    y = int(y)
    if x in r.keys():
        r[x] += y
    else:
        r[x] = y
    b.append((x, r[x]))
        
mx = max(r.values())

for x, p in b:
    if p >= mx and r[x] == mx:
        print x
        break
