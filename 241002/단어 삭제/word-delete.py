string = input()
word = input()

while(True):
    string = string.replace(word, "")
    if word not in string:
        break
print(string)