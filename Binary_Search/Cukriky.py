def can_distribute(arr, top, n):
    temp_arr = arr[:]  # Vytvoriť kópiu poľa
    for i in range(len(temp_arr)):
        if temp_arr[i] > top:
            temp_arr[i] = top
    return sum(temp_arr) >= n

def find_min(arr, min_num, total_num):
    low, high = 0, min_num
    result = "Nic nedostanete"

    while low <= high:
        mid = (low + high) // 2
        if can_distribute(arr, mid, total_num):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

input1 = [int(i) for i in input().split()]
input2 = [int(i) for i in input().split()]

number_of_candy = input1[1]
ceiling = max(input2)

print(find_min(input2, ceiling, number_of_candy))

