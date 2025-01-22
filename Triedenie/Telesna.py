x = input()
input1 = [int(i) for i in input().split()]
x = input()
input2 = [int(i) for i in input().split()]

ptr1 = 0
ptr2 = 0
final_list = []

while ptr1 < len(input1) and ptr2 < len(input2):
    if input1[ptr1] == input2[ptr2]:
        final_list.append(input1[ptr1])
        final_list.append(input2[ptr2])
        ptr1 += 1
        ptr2 += 1
    elif input1[ptr1] < input2[ptr2]:
        final_list.append(input1[ptr1])
        ptr1 += 1
    else:
        final_list.append(input2[ptr2])
        ptr2 += 1


final_list.extend(input1[ptr1:])
final_list.extend(input2[ptr2:])

print(" ".join(map(str, final_list)))
