def isConsecutive (n):
    if (n & (n - 1)) == 0:
        return False
    else:
        return True
    
a1 = isConsecutive(4)
print (a1)

a2 = isConsecutive(7)

print (a2)

a3 = isConsecutive(8)
print (a3)

a4 = isConsecutive(15)
print (a4)

