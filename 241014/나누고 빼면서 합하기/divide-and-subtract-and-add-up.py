n, m = map(int, input().split())
arr= list(map(int, input().split()))

def check_m(m):
    if m % 2 == 0:
        m = int(m / 2)
    else:
        m -= 1
    return m 

def sum_idxm(arr, m):
    sum = arr[m - 1]
    while m >1:
        m = check_m(m)
        sum += arr[m-1]
    return sum

print(sum_idxm(arr, m))