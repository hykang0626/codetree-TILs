a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if 1920%i == 0 and 2880%i == 0:
        cnt+=1
    
if cnt >0:
    print("1")
else : 
    print("0")