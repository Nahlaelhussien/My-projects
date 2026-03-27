n, s = map(int, input().split())
l = list(map(int, input().split()))

left = 0
s_sum = 0
ans = 0

for right in range(n):
    s_sum += l[right]

    while s_sum > s:
        s_sum -= l[left]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)
