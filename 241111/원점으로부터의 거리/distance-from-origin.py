class dot:
    def __init__ (self, x, y, num):
        self.x = x
        self.y = y
        self.num = num

dots = []
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    dots.append(dot(x, y, i+1))

dots.sort(key = lambda dot : abs(dot.x) + abs(dot.y))

for d in dots:
    print(d.num)