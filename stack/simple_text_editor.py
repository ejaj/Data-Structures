stack = []
string = ""
for _ in range(int(input())):
    args = input().split()
    if args[0] == '1':
        stack.append(string)
        string += args[1]
    elif args[0] == '2':
        stack.append(string)
        string = string[:-int(args[1])]
    elif args[0] == '3':
        print(string[int(args[1])-1])
    else:
        string = stack.pop()
