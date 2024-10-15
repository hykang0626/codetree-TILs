n = int(input())
arr = list(map(int, input().split()))

arr.sort()
group = []
# print(arr)
for i in range(n):
    group.append(arr[i] + arr[2 * n - i -1])
    # print(arr[i] , arr[2 * n - i -1])
print(max(group))