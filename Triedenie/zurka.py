nothing = input()

inputs = [int(i) for i in input().split()]
len_list = len(inputs)
inputs_sorted = sorted(inputs)


diff = 0


for i in range(0,len_list):
    if inputs[i] != inputs_sorted[i]:
        diff+=1

if diff == 2 or diff == 0 :
    print("Maja")
else:
    print("neMaja")
