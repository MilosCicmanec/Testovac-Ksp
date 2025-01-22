n1 = 0
n2 = 1
n3 = 0
l = int(input())
s = ""
if l == 1:
    print(0)
elif l == 2:
    print("0 1")
else:
    s = s + str(n1)
    s = s + " "
    s = s + str(n2)
    s = s + " "
    for i in range(l-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        s = s + str(n3)
        s = s + " "
print(s.rstrip())


