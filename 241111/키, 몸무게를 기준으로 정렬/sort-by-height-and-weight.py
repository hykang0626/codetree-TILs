class person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

people = []
n = int(input())

for i in range(n):
    name, h, w = input().split()
    people.append(person(name, int(h), int(w)))

people.sort(key = lambda person : (person.h, -person.w))

for p in people:
    print(p.name, p.h, p.w)