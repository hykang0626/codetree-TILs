class student:
    def __init__(self, h, w, num):
        self.h = h
        self.w = w
        self.num = num
        

n = int(input())
students = []

for i in range(n):
    h, w = tuple(input().split())
    students.append(student(int(h),int(w), i+1))

students.sort(key = lambda student : (-student.h, -student.w))

for  student in students:
    print(student.h, student.w, student.num)