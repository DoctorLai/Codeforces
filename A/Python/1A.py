s = raw_input("")

ss = s.split(" ")
n = int(ss[0])
m = int(ss[1]);
a = int(ss[2]);

if (n < m):
    t = n
    n = m
    m = t

sum = 1
top = 0
if (n > a):
    if (n % a == 0):
        s = n / a
    else:
        s = n / a + 1
    top = s
    sum = top

if (m > a):
    m -= a
    if (m % a == 0):
        temp = m / a
    else:
        temp = m / a + 1
    sum = sum + (temp * top)
    

print sum