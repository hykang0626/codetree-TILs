n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
def check_list(a, b):
    for i in range (n):
        if a[i] != b[i]:
            return False
    return True
if check_list(a, b):
    print("Yes")
else:
    print("No")