def num369(n):
    while n > 0:
        if (n % 10 == 3 or n % 10 == 6 or n % 10 == 9):
            return True
        n = n//10
    return False
  

def multi3(n):
    return n%3 == 0

a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if num369(i) or multi3(i):
        cnt +=1
print(cnt)