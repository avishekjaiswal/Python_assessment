a=raw_input()
letters=0
digits=0
for c in a:
    if c.isdigit():
        digits = digits + 1
    else:
        letters=letters + 1

print "Letters s" ,letters
print "Digits" ,digits