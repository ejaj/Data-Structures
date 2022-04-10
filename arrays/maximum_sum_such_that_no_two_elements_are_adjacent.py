def find_max_sum(arr):
    incl = arr[0]
    excl = 0
    for i in range(1, len(arr)):
        new_excel = excl if excl>incl else incl
        incl = excl + arr[i]
        excl = new_excel
    return excl if excl > incl else incl


arr = [5, 5, 10, 100, 10, 5]
print(find_max_sum(arr))