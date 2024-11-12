m1, d1, m2, d2 = map(int, input().split())

day_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start = d1
for i in range(m1-1):
    start += days[i]

finish = d2 
for i in range(m2-1):
    finish += days[i]

day = finish- start +1

print(day_of_week[day%7])