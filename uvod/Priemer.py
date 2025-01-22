import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
# Načítanie päť čísel oddelených medzerou
nums = [a,b,c,d,e]
x = 0  # Inicializácia x
for n in nums:
    x += n
average = x / len(nums)
print(math.floor(average))  # Zaokrúhlenie nadol a výpis výsledku

