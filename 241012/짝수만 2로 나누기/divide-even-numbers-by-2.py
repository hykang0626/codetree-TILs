def change_list(_list):
    for i in range(len(_list)):
        if (_list[i]%2 == 0):
            _list[i] = int(_list[i] / 2)
    return _list
 
n = int(input())

_list = list(map(int, input().split()))

print(*change_list(_list))