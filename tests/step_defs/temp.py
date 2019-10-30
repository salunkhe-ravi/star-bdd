arr = [1, 2, 3, 8, 5, 6]
for i in range(1, 4):
    arr[i - 1] = arr[i]
    print(arr[i - 1], end="....")
for i in range(0, 6):
    print(arr[i], end=" ")
