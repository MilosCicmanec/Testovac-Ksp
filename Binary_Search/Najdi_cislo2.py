n = int(input())

inputs = [int(i) for i in input().split()]
n = int(input())
questions = []
inputs_dict = {value: index for index, value in enumerate(inputs)}

for i in range(n):
    questions.append(int(input()))

for i in questions:
    if i in inputs_dict or -abs(i) in inputs_dict:
        print("A")
    else:
        print("N")