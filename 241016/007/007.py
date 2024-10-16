class test:
    def __init__(self, code, point, time):
        self.code = code
        self.point = point
        self.time = time

s1, s2, s3 = input().split()
secret = test(s1, s2, s3)
print("secret code :", secret.code)
print("meeting point :", secret.point)
print("time :", secret.time)