#!/usr/bin/env python

n, k = map(int, raw_input().split())
num = map(int, raw_input().split())

cnt = len([i for i in num if i <= 0])
ans = 0

if cnt >= k:
    for i in xrange(len(num)):
        if num[i] <= 0:
            if k > 0:
                num[i] = -num[i]
                k -= 1
            else:
                break
    print sum(num)
else:
    y = abs(num[0])
    for i in xrange(len(num)):
        if num[i] <= 0:
            num[i] = -num[i]
        if num[i] < y:
            y = num[i]            
    k -= cnt
    if (k & 1) == 0:
        print sum(num)
    else:        
        print sum(num) - 2 * y
        
