days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())

start = d1
for i in range(m1 -1):
    start += days[i]

finish = d2
for i in range(m2-1):
    finish += days[i]

print(finish - start +1)