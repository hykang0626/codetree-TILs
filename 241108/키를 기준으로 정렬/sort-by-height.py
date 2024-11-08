class person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())

people = []
for i in range(n):
    name, h, w = tuple(input().split())
    people.append(person(name, h, w))

people.sort(key = lambda person : person.h)

for i in range(n):
    print(people[i].name, people[i].h, people[i].w)