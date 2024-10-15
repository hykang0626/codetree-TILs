n = int(input())
words = []
for i in range (n):
    w = input()
    words.append(w)
words.sort()
for i in range(n):

    print(words[i])