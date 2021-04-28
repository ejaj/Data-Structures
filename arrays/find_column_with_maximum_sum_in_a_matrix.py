import sys
N = 5
def colMaxSum(mat):
    idx = -1
    maxSum = -sys.maxsize
    for i in range(0,N):
        sum = 0
        for j in range(0, N):
            sum += mat[j][i]
        if sum > maxSum:
            maxSum = sum
            idx = i
    return idx, maxSum


mat = [[1, 2, 3, 4, 5],
       [5, 3, 1, 4, 2],
       [5, 6, 7, 8, 9],
       [0, 6, 3, 4, 12],
       [9, 7, 12, 4, 3]]

ans, ans0 = colMaxSum(mat)

print("Column", ans + 1, "has max Sum", ans0)