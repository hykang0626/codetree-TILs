class score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

scores = []
for i in range(n):
    na, k, e, m = tuple(input().split()) 
    scores.append(score(na, int(k), int(e), int(m)))

scores.sort(key = lambda score:(-score.kor, -score.eng, -score.math))

for score in scores:
    print(score.name, score.kor, score.eng, score.math)