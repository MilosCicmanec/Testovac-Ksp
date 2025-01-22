n = int(input())

temp = [i for i in input().split()]
inputs = []

for i in temp:
    inputs.append(int(i))
n = min(inputs)

num_times = 0

for i in inputs:
    if i == n:
        num_times += 1
print(num_times)

