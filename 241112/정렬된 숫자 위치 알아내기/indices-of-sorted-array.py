class seq:
    def __init__ (self, num):
        self.num = num

n = int(input ())
numbers = []
l = list(map(int, input().split()))

for i in range(n):
    numbers.append(seq(l[i]))

numbers.sort(key = lambda seq : seq.num)


for idx, num in enumerate(numbers, start = 1):
    num.idx = idx
l_idx = []
for i in range(n):
    for j in range(n):
        if l[i] == numbers[j].num:
            if numbers[j].idx not in l_idx:
                # print(numbers[j].num, numbers[j].idx)
                l_idx.append(numbers[j].idx)
                break

print(*l_idx)