def LinearSearch(arr, t):
    for i in range (len(arr)):
        if arr[i] == t:
            return i
    return -1




a1 = LinearSearch([1, 2, 3, 4, 5], 3)

print(a1)

arr1 = [10, 20, 30, 40, 50]
xc = LinearSearch(arr1, 25)
print(xc)


