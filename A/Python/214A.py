#!/usr/bin/env python
# http://acm.zhihua-lai.com

n, m = map(int, raw_input().split(' '))

x = 0
for a in xrange(0, int(n ** 0.5) + 1):
    b = n - a * a
    if b >= 0 and a + b * b == m:
        x += 1

print x
