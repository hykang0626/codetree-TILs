def Print(n, m):
    for i in range(n):
        print("1" * m)

n, m = map(int, input().split())
Print(n,m)