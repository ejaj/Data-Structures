import sys
N = 5
def rowMaximum(matrix):
    idx = -1
    maxSum = -sys.maxsize
    for i in range(0,N):
        sum = 0
        for j in range(0,N):
            sum += matrix[i][j]
        if sum > maxSum:
            maxSum = sum
            idx = i
    res = [idx, maxSum]
    return res


mat = [[1, 2, 3, 4, 5],
       [5, 3, 1, 4, 2],
       [5, 6, 7, 8, 9],
       [0, 6, 3, 4, 12],
       [9, 7, 12, 4, 3]]

ans = rowMaximum(mat)
print("Row", ans[0] + 1, "has max sum", ans[1])