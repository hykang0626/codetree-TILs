class student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num

n = int(input())
students = []

for i in range(n):
    h, w= map(int, input().split())
    students.append(student(h, w, i+1))

students.sort(key = lambda student : (student.h, -student.w))

for s in students:
    print(s.h, s.w, s.num)