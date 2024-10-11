def func(n, m):
    
    start = max(n, m)
    while True:
        if start%n == 0 and start%m == 0:
            print(start)
            break
        start += 1
    
n, m = map(int, input().split())
func(n, m)