#!/usr/bin/env python

h = [0] * 101
a = [0] * 101
for _ in xrange(int(input())):
    x, y = map(int, raw_input().split())
    h[x] += 1
    a[y] += 1
print sum(x[0]*x[1] for x in zip(h, a))
