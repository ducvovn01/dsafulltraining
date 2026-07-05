def CheckPrime(n):
    if n <= 1:
        return False
    for i in range (2, int (n ** 0.5) + 1):
        if n % i == 0:
            return False
        return True
    





a1 = CheckPrime(7)

print(a1)


a2 = CheckPrime(10)

print(a2)
