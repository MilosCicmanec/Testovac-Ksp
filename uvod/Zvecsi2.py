n = int(input())

temp = [i for i in input().split()]
inputs = []

for i in temp:
    inputs.append(int(i))
x = int(input())
s = ""

for i in inputs:
    s = s + str(i+x)
    s = s + " " 

print(s.rstrip())

