def multi(a, b):
    number = 1
    for i in range (b):
        number *=a
        
    return number
    
a, b = map(int, input().split())
print(multi(a, b))