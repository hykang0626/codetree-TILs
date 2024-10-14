def _abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])
    print(*arr)

n = int(input())
arr = list(map(int, input().split()))
_abs(arr)