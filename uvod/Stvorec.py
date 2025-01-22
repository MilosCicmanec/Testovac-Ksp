a = int(input())
square = []
s = ""
Strings = []
for i in range(a):
    square.append([int(i) for i in input().split()])

for i in range(a):
    for x in range(a):
        s = s + str(square[x][i])
        s = s + " "
    Strings.append(s.rstrip())
    s = ""
Strings.reverse()
for i in Strings:
    print(i)
