n = int(input())
arr = list(map(int, input().split()))
mid_number = []
for i in range (len(arr)):
    if (i+1)%2 == 1:
        mid_number.append(arr[i//2])
print(*mid_number)