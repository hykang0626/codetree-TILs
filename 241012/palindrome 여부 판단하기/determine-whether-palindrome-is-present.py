def check_string(a):
    check = 0
    for i in range (len(a)):
        if a[i] == a[len(a)-i-1]:
            check+=1
    if check == len(a):
        return True
    return False
a = input()
if check_string(a):
    print("Yes")
else:
    print("No")