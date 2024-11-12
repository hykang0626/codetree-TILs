a, b, c = map(int, input().split())

start = 11 * 60 * 24 + 11 * 60 + 11
finish =  a * 60 * 24 + b * 60 + c

if finish - start < 0:
    print(-1)
else:
    print(finish - start)