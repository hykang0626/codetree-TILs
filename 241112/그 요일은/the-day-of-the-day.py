m1, d1, m2, d2 = map(int, input().split())
check_day = input()

week_of_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
days = [31, 28, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start = d1
for i in range(m1-1):
    start+=days[i]

# start % 7 ->월요일인 인덱스, start %7 -1 = 월요일인덱스와의 차이
find = start % 7
# print(find)
for i in range(7):
    if week_of_day[i] == check_day:
        check_idx = i - find
        # print(check_idx)

finish = d2
for i in range(m2-1):
    finish += days[i]

start_check = start // 7
if start % 7 >= check_idx:
    start_check += 1

fin_check = finish // 7
# print(finish)
if finish % 7 >= check_idx:
    fin_check += 1

# print(start_check, fin_check)
print(fin_check - start_check)

