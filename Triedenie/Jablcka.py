inputs = [int(i) for i in input().split()]
pivot = inputs[1]


inputs = [int(i) for i in input().split()]

left = [i for i in inputs if i < pivot]
mid = [i for i in inputs if i == pivot]
right = [i for i in inputs if i > pivot]

print(" ".join(map(str,left)))
print(" ".join(map(str,mid)))
print(" ".join(map(str,right)))