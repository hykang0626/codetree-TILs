def f(n, arr):
    if n == 0:
        return arr[n]
    return max (arr[n-1], f(n-1, arr))
n = int(input())
arr = list(map(int, input().split()))
print(f(n, arr))