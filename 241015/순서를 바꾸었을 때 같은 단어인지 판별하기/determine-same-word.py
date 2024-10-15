a = input()
b = input()
l_a = list(a)
l_b = list(b)
l_a.sort()
l_b.sort()
def check(a, b):
    if len(a) != len(b):
        return False
    for i in range(len(l_a)):
        if l_a[i] != l_b[i]:
            return False
    return True

if check(l_a, l_b):
    print("Yes")
else:
    print("No")