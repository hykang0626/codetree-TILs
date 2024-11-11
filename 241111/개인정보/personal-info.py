class person:
    def __init__(self, n, h, w):
        self.n = n
        self.h = h
        self.w = w

people = []
for i in range(5):
    n, h, w = tuple(input().split())
    people.append(person(n, int(h), float(w)))

print("name")
people.sort(key = lambda person : person.n)
for p in people:
    print(p.n, p.h, p.w)

print("")
print("height")
people.sort(key = lambda person : -person.h)
for p in people:
    print(p.n, p.h, p.w)