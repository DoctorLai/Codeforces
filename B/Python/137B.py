n = int(raw_input())
s = raw_input().split(" ")
ss = map(int, s)

ans = 0
i = 0
k = []
while i < n:
    if s[i] in k or ss[i] > n:
        ans += 1                    
    else:
        k.append(s[i])
    i += 1

print ans