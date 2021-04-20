def prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return 'Простое число' if counter == 2 else 'Составное число'


n = int(input())
lst = [int(s) for s in input().split()]
ls = []
for i in lst:
    ls.append(lst.count(i))
print(ls)