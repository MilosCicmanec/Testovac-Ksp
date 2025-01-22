a = int(input())
stars = []
for i in range(a, 0, -1):  # Začíname od a a klesáme k 1
    row = "*" * i  # Vytvorí riadok s i hviezdičkami
    stars.append(row)

for row in stars:
    print(row)
