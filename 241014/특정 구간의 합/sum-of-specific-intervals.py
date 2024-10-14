n, m = map(int, input().split())
a = list(map(int, input().split()))

def sum_values(a1, a2):
    global a
    sum = 0
    for i in range(a1 - 1, a2):
        sum += a[i]
    return sum

for i in range (m):
    a1, a2 = map(int, input().split())
    sum = sum_values(a1, a2)
    print(sum)