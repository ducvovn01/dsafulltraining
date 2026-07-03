#We use quotient approach to find the minimum difference between two numbers


def MinDiff(a, b):
    q = a // b

    n1 = q * b
    n2 = (q + 1) * b


    if abs(a - n1) < abs(a - n2):
        return n1
    else:
        return n2
    

a = MinDiff(20, 6)

print (a)

b = MinDiff(20, 7)


print (b)


