n = int(input())

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
ar=[]
def in_range(x, y):
    return x>=0 and x<n and y>=0 and y<n
for i in range(n):
    a= list(map(int, input().split()))
    ar.append(a)
count=0

for x in range(n):
    for y in range(n):
        cnt=0
        for dx, dy in zip(dxs, dys):
            nx, ny = x+ dx, y + dy
            if in_range(nx, ny) and ar[nx][ny] ==1:
                cnt+=1
        if cnt>=3:
            count+=1
print(count)