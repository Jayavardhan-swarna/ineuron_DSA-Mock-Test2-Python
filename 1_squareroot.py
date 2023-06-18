def Sqrt(x):
    if x == 0:
        return 0

    left = 1
    right = x

    while left <= right:
        mid = (left + right) // 2

        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid - 1

    return right

print(Sqrt(4)) #output:2
print(Sqrt(8)) #output:2
