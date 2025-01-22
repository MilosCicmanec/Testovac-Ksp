l = int(input())
row = ""
row_lenght =int((2*l)-1)
num_dots = 0
list = []

for i in range(l,0,-1):
    num_dots = row_lenght - int((2*i)-1)
    for _ in range(num_dots//2):
        row = row + "."
    for _ in range(int((2*i)-1)):
        row = row + "*"
    for _ in range(num_dots//2):
        row = row + "."
    list.append(row)
    row = ""
list.reverse()
for i in list:
    print(i)
