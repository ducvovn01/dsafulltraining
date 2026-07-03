#In this exercise, we will use the recursive approach

def Sum(n):
    if n == 1:
        return 1
    
    else:
        return n + Sum(n - 1)
    


a = Sum(5)

print (a)

b = Sum(15)

print (b)

c = Sum(1)

print (c)

