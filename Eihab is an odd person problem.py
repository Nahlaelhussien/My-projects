n = int(input())
l = list(map(int, input().split()))

has_even = any(x % 2 == 0 for x in l)
has_odd = any(x % 2 == 1 for x in l)

if has_even and has_odd:
    l.sort()

print(*l)
