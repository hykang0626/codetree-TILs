class Student:
    def __init__(self, id = 'codetree', level = 10):
        self.id = id
        self.level = level
student1 = Student()
print("user", student1.id, "lv", student1.level)

id, level = input().split()
student1.id = id
student1.level =level
print("user", student1.id, "lv", student1.level)