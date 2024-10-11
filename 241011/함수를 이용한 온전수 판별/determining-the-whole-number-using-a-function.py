def is_number(n):
    if n%2 == 0:
        return False
    if n%10 == 5:
        return False
    if n%3 == 0 and n%9 != 0:
        return False
    return True
cnt=0
a, b = map(int, input().split())
for i in range(a, b+1):
    if is_number(i):
        cnt+=1
print(cnt)