def is_date(m, d):
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m <= 12:
        if day[m-1] >= d:
            return True
    return False
m, d = map(int, input().split())
if is_date(m, d):
    print("Yes")
else:
    print("No")