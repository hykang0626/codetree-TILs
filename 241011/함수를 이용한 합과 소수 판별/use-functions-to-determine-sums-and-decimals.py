def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def Sum(n):
    sum = 0
    while n>0:
        sum+= n%10
        n = n//10

    if (sum % 2 == 0):
        return True
    return False

a, b = map(int, input().split())
cnt = 0 
for i in range( a, b+1):
    if (is_prime(i) and Sum(i)):
        cnt+=1
print(cnt)