class weather:
    def __init__(self, date, day, wea):
        self.date = date
        self.day = day
        self.wea = wea

n = int(input())
info = []

for i in range(n):
    d1, d2, w = tuple(input().split())
    info.append(weather(d1, d2, w))

for i in range(n):
    if info[i].wea == 'Rain':
        print(info[i].date, info[i].day, info[i].wea)
        break