def check_arr(a, b):
    for i in range(len(a)):
        if (b[0] == a[i]):
            for j in range(len(b)):
                if i + j <len(a):
                    if(b[j]!=a[i+j]):
                        return False
    return True

n1, n2 = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))
if check_arr(a, b):
    print("Yes")
else:
    print("No")