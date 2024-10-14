def _print(n):
    if n == 0:
        return
    _print(n - 1)
    print("HelloWorld")

n = int(input())

_print(n)