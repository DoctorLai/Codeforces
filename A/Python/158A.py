s = raw_input().split(" ")
n = int(s[0])
k = int(s[1])

s = raw_input().split(" ")
s = map(int, s)

ans = 0

for i in s:
    if i > 0 and i >= s[k - 1]:
        ans += 1

print ans