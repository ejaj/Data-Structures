def waiter(number, q):

    primegen = [1] * 10000
    prime = []
    for i in range(2, 10000):
        if primegen[i] == 1:
            for j in range(i,10000,i):
                primegen[j] = 0
            prime.append(i)
    a = [[] for i in range(q+1)]
    b = [[] for i in range(q+1)]
    a[0] = number

    for i in range(q):
        while a[i]:
            plate = a[i].pop()
            if plate%prime[i] == 0:
                b[i+1].append(plate)
            else:
                a[i+1].append(plate)
    result = []
    for i in range(q+1):
        while b[i]:
            result.append(b[i].pop())
    for i in range(q+1):
        while a[i]:
            result.append(a[i].pop())
    return result