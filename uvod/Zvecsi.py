n = int(input())
x = int(input())
s = ""
temp = 0
for i in range(n):
    temp = int(input())
    temp += x
    s = s + str(temp)
    s = s + " "

print(s.rstrip())


