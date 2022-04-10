def twoStacks(maxSum, a, b):
    maxnum = total = i = j = 0
    while i < len(a) and total + a[i] <= maxSum:
        total += a[i]
        i += 1
        maxnum += 1
    while j < len(b) and i >= 0:
        total += b[j]
        j += 1
        while i > 0 and total > maxSum:
            i -= 1
            total -= a[i]
        if total <= maxSum and maxnum < i + j:
            maxnum = i + j

    return maxnum


a = [4, 2, 4, 6, 1]
b = [2, 1, 8, 5]
maxSum = 10

print(twoStacks(maxSum, a, b))
