n = int(input())
output = 0
temp = [i for i in input().split()]
inputs = []

for i in temp:
    inputs.append(int(i))

x = int(input())

temp = []

for i in inputs:
    if i < x:
        temp.append(i)
for i in temp:
    output += i
print(output)
