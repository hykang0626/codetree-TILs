days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())

sum = days[m1-1] - d1 + 1 + d2
for i in range (m1+1, m2):
    sum += days[i]

print(sum)