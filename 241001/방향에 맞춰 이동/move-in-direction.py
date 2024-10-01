n=int(input())
dx=[1,0, -1, 0]
dy = [0, -1, 0, 1]
x=0
y=0
for i in range(n):
    a, b= input().split()
    b=int(b)
    if (a=='N'):
        dir_num=3
    elif (a == 'E'):
        dir_num =0
    elif (a=='W'):
        dir_num =2
    else:
        dir_num=1
    x = x + dx[dir_num]*b
    y = y + dy[dir_num]*b
    
print(x, y)