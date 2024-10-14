def check_alphabet(a):
    check = []
    for i in range(len(a)):
        if a[i] not in check:
            check.append(a[i])
    if len(a)>=2:
        return True
    return False

s = input()
if check_alphabet(s):
    print("Yes")
else:
    print("No")