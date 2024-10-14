def f(n, cnt):
    # print(cnt, n)
    if n == 1 :
        return cnt
    if n % 2 == 0:
        cnt+=1
        return f(n // 2, cnt)
    else: 
        cnt+=1
        return f(n // 3, cnt) 
    


n = int(input())
cnt = 0
print(f(n, cnt))