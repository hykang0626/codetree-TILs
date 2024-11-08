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

minyear = 2100
mininfo = info[0]
for i in range(n):
    
    if info[i].wea == 'Rain' and int(info[i].date[0:4]) < minyear:
        minyear = int(info[i].date[0:4])
        mininfo = info[i]
print(mininfo.date, mininfo.day, mininfo.wea)