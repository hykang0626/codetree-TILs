class score:
    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

n = int(input())
student = []
for i in range(n):
    name, s1, s2, s3 = tuple(input().split())
    student.append(score(name, int(s1), int(s2), int(s3)))

student.sort(key = lambda score : (score.s1+score.s2+ score.s3))

for s in student:
    print(s.name, s.s1, s.s2, s.s3)