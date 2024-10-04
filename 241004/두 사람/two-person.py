check=0
for i in range (2):
    age, gender=input().split()
    age = int(age)
    if age >19 and gender =='M':
        check+=1
if check>=1:
    print("1")
else:
    print("0")