# Nacitanie vstupnych hodnot
n, x = map(int, input().split())  # Prve riadok obsahuje n a x
input_numbers = list(map(int, input().split()))  # Druhy riadok obsahuje n cisel

# Overenie ci sa rozdiel medzi dvoma cislami rovna x
number_found = False

for i in input_numbers:
    if (i + x) in input_numbers or (i - x) in input_numbers:
        number_found = True
        break

# Vystup
if number_found:
    print("Ano")
else:
    print("Nie")

