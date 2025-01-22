parameters = [int(i) for i in input().split()]
inputs = []
for i in range(parameters[0]):
    inputs.append([int(i) for i in input().split()])
s = ""

for i in range(parameters[1]):
    for x in range(parameters[0]):
        s = s + str(inputs[x][i])
        s = s + " "
    print(s.rstrip())
    s = ""

