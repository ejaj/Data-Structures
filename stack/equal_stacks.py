def equal_stacks(h1, h2, h3):
    """
    :param h1:
    :param h2:
    :param h3:
    :return:
    """
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    while True:
        min_height = min(sum1, sum2, sum3)

        if min_height == 0:
            return 0
        if min_height < sum1:
            sum1 -= h1.pop()
        if min_height < sum2:
            sum2 -= h2.pop()
        if min_height < sum3:
            sum3 -= h3.pop()
        if sum1 == sum2 == sum2:
            return sum1
