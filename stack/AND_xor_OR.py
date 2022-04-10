def andXorOr(a):
    stack = []
    maxResult = 0
    for i in range(len(a)):
        while stack:
            result = stack[-1] ^ a[i]
            maxResult = max(maxResult, result)

            if stack[-1] > a[i]:
                stack.pop()
            else:
                break
        stack.append(a[i])

    return maxResult