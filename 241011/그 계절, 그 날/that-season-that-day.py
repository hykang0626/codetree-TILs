def check_year(y): #윤년체크
    if (y % 4 != 0):
        return False
    if (y % 100 ==0 and y % 400 != 0):
        return False
    return True

def check_day(y, m, d):
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_year(y): #윤년이면 
        if day[m-1] + 1>= d:
            return True
    else:
        if day[m-1] >= d:
            return True
    return False

def check_season(m):
    if m>=3 and m<=5:
        return "Spring"
    elif m>=6 and m<=8:
        return "Summer"
    elif m>=9 and m<=11:
        return "Fall"
    else:
        return "Winter"

y, m, d = map(int, input().split())


if check_day(y, m, d):
    print(check_season(m))
else:
    print("-1")