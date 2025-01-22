x = input()
inputs = [int(i) for i in input().split()]
sum_inputs = sum(inputs) //2
d_sum = 0
inputs.sort()
n = 0
while d_sum < sum_inputs:
    d_sum += inputs[-1]
    n += 1
    inputs.pop()
print(n)