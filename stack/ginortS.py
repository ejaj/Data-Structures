from __future__ import print_function

def func(x):
    if x.isalpha():
        if x.isupper():
            return (ord(x) - ord('A'))
        else:
            return (ord(x) - ord('a')) - 30
    else:
        if int(x) % 2 == 0:
            return 60 + int(x)
        else:
            return 30+int(x)
s = input()
map(lambda x:print(x,end=''), (sorted(s,key=func)))