#!/bin/env python
#http://www.zhihua-lai.com/acm
#http://codeforces.com/problemset/problem/347/B

n = int(raw_input())
a = map(int, raw_input().split())

c = 0
f = True
for x in xrange(n):
    if a[x] != x:
        if f and (a[a[x]] == x):
            c += 2
            f = False
    else:
        c += 1

if c == n:
    print c
else:
    print c if (not f) else c + 1
