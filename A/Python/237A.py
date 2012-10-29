#!/usr/bin/env python
# http://acm.zhihua-lai.com

n = int(raw_input())

a = dict()
ans = 1
xx = 1

for x in xrange(n):
    h, s = map(int, raw_input().strip().split(" "))
    t = h * 60 + s
    if a.has_key(t):
        ans += 1
        if ans > xx: xx = ans
    else:
        a[t] = True
        ans = 1

print xx
