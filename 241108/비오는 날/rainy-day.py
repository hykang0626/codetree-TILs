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

mindate = 21001212
mininfo = info[0]
for i in range(n):
    y, m, d = info[i].date.split('-')
    date = int(y)*10000+int(m ) * 100 +int(d)
    if info[i].wea == 'Rain' and date <= mindate:
        mindate = date
        mininfo = info[i]
print(mininfo.date, mininfo.day, mininfo.wea)