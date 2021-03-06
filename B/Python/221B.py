#!/usr/bin/env python
# http://www.zhihua-lai.com/acm

n = int(raw_input())
x = int(n ** 0.5)
ans = 0

def C(i, n):
    return 1 if any((ch for ch in str(i) if ch in n)) else 0
    
for i in xrange(1, x + 1):
    if n % i == 0:
        ans += C(i, str(n))
        if i * i != n:
            ans += C(n / i, str(n))

print ans
    
