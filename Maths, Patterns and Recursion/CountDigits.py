def DigitCounts(n):


    count = 0
    count = 1 + DigitCounts(n // 10) if n > 0 else 0
    return count



a1 = DigitCounts(12345)

print(a1)

a2 = DigitCounts(0)

print(a2)
print(DigitCounts(1234567890))

a3 = DigitCounts (1)


print(a3)