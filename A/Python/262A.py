#!/usr/bin/env python

n, k = map(int, raw_input().split())
s = raw_input().split()

ans = 0
for x in s:
    ans += 1 if x.count('4') + x.count('7') <= k else 0

print ans
