#!/usr/bin/env python
# http://www.zhihua-lai.com/acm

n = int(raw_input())

a = [False] * 26
ab = [False] * 26 * 26

for x in xrange(n):
    s = raw_input()
    for y in s:
        a[ord(y) - 97] = True
    for i in xrange(len(s) - 1):
        ab[(ord(s[i]) - 97) * 26 + ord(s[i + 1]) - 97] = True

found = False
for x in xrange(26):
    if a[x] == False:
        found = True
        print chr(97 + x)
        break

if not found:
    for x in range(26 * 26):
        if not ab[x]:
            print chr(97 + x / 26) + chr(97 + x % 26)
            break

    
