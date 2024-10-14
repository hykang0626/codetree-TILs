def number(n):
    if n == 0:
        return
    number(n - 1)
    print(n, end = " ")

def reverse_num(n):
    if n == 0:
        return
    print(n, end = " ")
    reverse_num(n - 1)
    

n = int(input())
number(n)
print("", end = "\n")
reverse_num(n)