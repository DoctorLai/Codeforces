#!/usr/bin/env python

a, b, n = map(int, raw_input().split())

a *= 10
for _ in xrange(10):
    if (a + _) % b == 0:
        print str(a + _) + "0" * (n - 1)
        exit()

print -1
