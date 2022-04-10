def poisonousPlants(p):
    stack = []
    maxday = 0
    for plant in p:
        day = 0
        while stack and stack[-1][0] >= plant:
            day = max(day, stack.pop()[1])
        if stack:
            day += 1
        else:
            day = 0
        maxday = max(maxday, day)
        stack.append([plant, day])
    return maxday