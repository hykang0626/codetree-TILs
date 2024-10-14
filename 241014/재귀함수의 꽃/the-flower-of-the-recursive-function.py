def _print(n):
    if(n == 0):
        return
    print(n, end = " ")
    _print(n - 1)
    print(n, end = " ")

n = int(input())
_print(n)