n = int(input())
inputs = [int(i) for i in input().split()]
n = int(input())

questions = [int(i) for i in input().split()]

# Preprocess inputs into a dictionary for O(1) lookups
inputs_dict = {value: index for index, value in enumerate(inputs)}

# Answer each question using the dictionary
for i in questions:
    if i in inputs_dict:
        print(inputs_dict[i])  # Print the index of the value
    else:
        print(-1)

