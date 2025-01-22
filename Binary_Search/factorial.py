def findTrailingZeros(n):
    
    if n < 0:
        return -1

    
    count = 0

    
    while n >= 5:
        n //= 5
        count += n

    return count

k = int(input())

def find(target):
    low = 0
    high = target * 5
    result = -1

    while low <= high:
        mid = (low + high) // 2
        zeros = findTrailingZeros(mid)
        
        if zeros >= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result

print(find(k))
