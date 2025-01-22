x = input()
inputs = [int(i) for i in input().split()]


smallest_index = inputs.index(min(inputs))


inputs[0], inputs[smallest_index] = inputs[smallest_index], inputs[0]


print(" ".join(map(str, inputs)))
