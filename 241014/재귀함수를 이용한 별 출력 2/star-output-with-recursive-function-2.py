def _print(n):
    if(n == 0):
        return
    print("* " * n)
    _print(n - 1)
    print("* " * n)

n = int(input())
_print(n)