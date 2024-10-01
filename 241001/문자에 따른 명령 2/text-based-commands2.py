dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
dir_num = 3 # 북 0동 1남 2서
x=0
y=0
str = input()
for i in range(len(str)):
    if str[i] == 'L':
        dir_num -=1
    elif str[i] == 'R':
        dir_num +=1
    elif str[i] == 'F':
        x+=dx[dir_num]
        y+=dy[dir_num]
print(x,y)