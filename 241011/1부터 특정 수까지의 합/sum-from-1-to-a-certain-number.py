def Sum(n):
    sum = 0
    for i in range (1, n + 1):
        sum += i
    return sum //10

n = int(input())
print(Sum(n))