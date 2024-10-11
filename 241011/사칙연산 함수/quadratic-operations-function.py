def Sum(a, c):
    return a + c
def Minus(a, c):
    return a - c
def Multi(a, c):
    return a * c
def Div(a, c):
    return a / c

a, o, c = input().split()
if o == '+':
    print(a, o, c, "=", Sum(int(a), int(c)))
elif o == '-':
    print(a, o, c, "=", Minus(int(a), int(c)))
elif o == '*':
    print(a, o, c, "=", Multi(int(a), int(c)))
elif o == '/':
    print(a, o, c, "=", Div(int(a), int(c)))
else:
    print("False")