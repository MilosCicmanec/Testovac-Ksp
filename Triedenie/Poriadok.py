x = input()
inputs = [int(i) for i in input().split()]


def sorted_ascending(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

def sorted_descending(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            sorted = False
    return sorted
if sorted_ascending(inputs) or sorted_descending(inputs):
    print("poriadok")
else:
    print("bordel")