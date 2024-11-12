m1, d1, m2, d2 = map(int, input().split())
check_day = input()

week_of_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days = [31, 28, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start = d1
for i in range(m1-1):
    start+=days[i]

# start % 7 ->월요일인 인덱스, start %7 -1 = 월요일인덱스와의 차이

finish = d2
for i in range(m2-1):
    finish += days[i]

sub_day = finish - start +1
count = sub_day // 7 
if sub_day % 7 > 0:
    # print(sub_day % 7)
    for i in range(sub_day % 7 + 1):
        if week_of_day[i] == check_day:
            count+=1

print(count)