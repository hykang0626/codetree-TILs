n = int(input())

def f(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        cnt += 1 
        return f(n // 2, cnt)
    else:
        cnt += 1
        return f(n * 3 + 1, cnt)
print(f(n, 0))