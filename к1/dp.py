n = int(input())
a = list(map(int, input().split()))
pos = [0] * (n + 1)
prev = [-1] * (n+1)
dp = [-10**6] + [10**6] * (n-1)


def upper_bound(a):
    left = 0
    right = n
    while right - left != 1:
        middle = (left + right) // 2
        if dp[middle] >= a:
            right = middle
        else:
            left = middle
    return right
for i in range(len(a)):
    r = upper_bound(a[i])
    dp[r] = a[i]
    prev[i] = r-1
    pos[r - 1] = 
print(max(prev) + 1)

