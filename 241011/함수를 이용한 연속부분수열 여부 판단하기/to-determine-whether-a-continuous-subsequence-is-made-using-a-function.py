def check_arr(a, b):
    for i in range(len(a)):
        flag = 0
        if (b[0] == a[i]):
            for j in range(len(b)):
                
                if(b[j]==a[i+j]):
                    flag+=1
            if (flag == len(b)):
                return True
    return False
                

n1, n2 = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))
if check_arr(a, b):
    print("Yes")
else:
    print("No")