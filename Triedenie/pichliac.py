n = int(input())
l = [9,9]
s = ""
if n < 3:
    print(-1)
else:
    for i in range(n-2):
        l.append(1)
    for i in l:
        s = s + str(i)
        s = s + " "
    print(s.rstrip())