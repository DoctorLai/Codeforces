
s = raw_input().split(" ")
n = int(s[0])
a = int(s[1])
b = int(s[2])

ans = 0
for i in range(1, n + 1):
    if i - 1 >= a and n - i<= b:
        ans += 1

print ans

