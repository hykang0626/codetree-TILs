def calc(a, b):
    if a > b:
        a = a + 25
        b = b * 2
    elif b > a:
        a = a * 2
        b = b + 25
    return a, b

a, b = map(int, input().split())

a, b = calc(a, b)
print(a, b)