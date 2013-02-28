#!/usr/bin/env python

n = int(raw_input())
d = map(int, raw_input().split())
s, t = map(int, raw_input().split())


if s > t:
    s, t = t, s

d1 = sum(d[s-1:t-1])
d2 = sum(d[t-1:]) + sum(d[:s-1])

print min(d1, d2)