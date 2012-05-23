r1 = raw_input("")
r2 = raw_input("")
r3 = raw_input("")

def chk():
    return (r1[0] == r3[2]) and (r1[1] == r3[1]) and (r1[2] == r3[0]) and (r2[0] == r2[2])

if chk():
    print "YES"
else:
    print "NO"
    