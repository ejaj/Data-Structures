def largestRectangle(h):
    stack = []
    max_area = index = 0

    while index < len(h):
        if not stack or h[stack[-1]] <= h[index]:
            stack.append(index)
            index += 1

        else:
            top_of_stack = stack.pop()
            area = (h[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            max_area = max(max_area, area)
    while stack:
        top_of_stack = stack.pop()
        area = (h[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))

        max_area = max(max_area, area)
    print(max_area)


hist = [1, 2, 3, 4, 5]
largestRectangle(hist)
