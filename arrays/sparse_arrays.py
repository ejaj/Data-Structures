from collections import Counter

'''
string = ['ab', 'ab', 'abc']
quires = ['ab', 'abc', 'bc']
output = [2,1,0]
'''


def matching_strings_count(strings, queries):
    """
    Matching String Count
    :param strings:
    :param queries:
    :return:
    """
    s = Counter(strings)
    result = []
    for q in queries:
        result.append(s[q])

    return result


def main():
    string = ['ab', 'ab', 'abc']
    quires = ['ab', 'abc', 'bc']
    print (matching_strings_count(string, quires))


if __name__ == '__main__':
    main()
