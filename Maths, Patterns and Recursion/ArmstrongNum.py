def DigitCounts(n):


    i = 0
    i = 1 + DigitCounts(n // 10) if n > 0 else 0
    return i



def ArmstrongNum(n):
    num = n
    sum = 0

    while num > 0:
        d = num % 10
        sum += pow(d, DigitCounts(n))
        num //= 10
    

    if sum == n:
        return True
    else:
        return False
    

a1 = ArmstrongNum(153)

print(a1)

a2 = ArmstrongNum(123)

print(a2)



