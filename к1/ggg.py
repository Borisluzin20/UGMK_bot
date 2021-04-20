l = int(input())
r = int(input())
a = int(input()) - 1
c = 0
i = l
j = i + a
while j<=r:
    c += 1ц
    i += a
    j += a
if c >= 2:
    print(c)
else:
    print(0)


