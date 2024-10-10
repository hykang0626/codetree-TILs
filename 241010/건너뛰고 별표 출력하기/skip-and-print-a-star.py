n = int(input())

for i in range (n):
    print("*" *(i+1), end = "\n\n")

for i in range (n-1, 0, -1):
    print("*"*i, end = "\n\n")