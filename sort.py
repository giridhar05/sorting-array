n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for num in arr:
    print(num, end=" ")
