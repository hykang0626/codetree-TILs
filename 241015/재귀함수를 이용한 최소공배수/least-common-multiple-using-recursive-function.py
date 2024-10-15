n = int(input())

arr = list(map(int, input().split()))

def f(n):
    global arr
    cnt = 0
    for i in arr:
        if n % i == 0:
            cnt += 1
    if cnt  == len(arr):
        return n
    return f(n + 1)

print(f(max(arr)))