#!/usr/bin/env python

for i in xrange(1, 6):
    s = map(int, raw_input().split())
    for k in xrange(1, 6):
        if s[k - 1] == 1:
            print abs(i - 3) + abs(k - 3)
            break
