n = int(input())  # Počet čísel
nums = [int(i) for i in input().split()]  # Načítanie čísel do zoznamu

while len(nums) > 1:  # Pokračujeme, kým nezostane jedno číslo
    temp = []  # Zoznam pre ďalšiu úroveň
    for i in range(len(nums) - 1):  # Prechádzame dvojice susedných čísel
        temp.append(nums[i] + nums[i + 1])  # Súčet susedných čísel
    nums = temp  # Prejdeme na ďalšiu úroveň
    print(" ".join(map(str, nums)))  # Vypíšeme novú úroveň

