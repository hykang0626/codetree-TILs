def check_t(s, t):
    for i in range(len(t)):
        if s[i] != t[i]:
            return False
    return True

n, k, t = input().split()
n = int(n)
k = int(k)
strings = []
for i in range (n):
    s = input()
    if check_t(s, t):
        strings.append(s)

strings.sort()
print(strings[k-1])