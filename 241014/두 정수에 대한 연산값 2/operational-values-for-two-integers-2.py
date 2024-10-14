def calc(a, b):
    if a > b:
        a *= 2
        b += 10
    if b > a:
        b *=2
        a += 10
    return a, b
a, b = map(int, input().split())
a, b = calc(a, b)
print(a, b)