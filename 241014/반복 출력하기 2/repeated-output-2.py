def _print(n):
    if n == 0:
        return
    _print(n - 1)
    print("HelloWorld")

_print(4)