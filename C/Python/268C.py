#!/usr/bin/env python
n, m = map(int, raw_input().split())
k = min(n, m)
print k + 1
for x in xrange(k + 1):
    print x, k - x
