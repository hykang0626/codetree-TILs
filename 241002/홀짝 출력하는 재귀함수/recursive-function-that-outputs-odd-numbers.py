n = int(input())

if (n%2 ==0):
    for i in range (1,n+1):
        if (i%2 ==0):
            print(i, end = " ")
elif (n%2 ==1):
    for i in range (1, n+1):
        if (i%2 ==1):
            print(i, end = " ")