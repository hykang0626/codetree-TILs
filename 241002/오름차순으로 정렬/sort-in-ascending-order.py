n = int(input())
array = list(map(int, input().split()))
tmp =0
for i in range(len(array)):
    for j in range(i, len(array)):
        if array[i]> array[j]:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

print(*array)