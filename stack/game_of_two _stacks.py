def two_stacks(max_sum, a, b):
    """
    :param max_sum:
    :param a:
    :param b:
    :return:
    """
    max_num = total = i = j = 0
    while i < len(a) and total + a[i] <= max_sum:
        total += a[i]
        i += 1
        max_num += 1
    while j < len(b) and i >= 0:
        total += b[j]
        j += 1
        while i > 0 and total > max_sum:
            i -= 1
            total -= a[i]
        if total <= max_sum and max_num < i + j:
            max_num = i + j

    return max_num


def main():
    a = [4, 2, 4, 6, 1]
    b = [2, 1, 8, 5]
    max_sum = 10
    print(two_stacks(max_sum, a, b))


if __name__ == '__main__':
    main()
