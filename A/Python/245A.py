#!/usr/bin/env python

ax = asum = 0
bx = bsum = 0

for i in xrange(int(raw_input())):
    t, x, y = map(int, raw_input().split())
    if t == 1:
        ax += x
        asum += 10
    else:
        bx += x
        bsum += 10

print "LIVE" if ax + ax >= asum else "DEAD"
print "LIVE" if bx + bx >= bsum else "DEAD"




