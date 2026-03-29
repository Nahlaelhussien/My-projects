n = int(input())
for i in range(n):
    w = input().strip()
    length = len(w)
    if length > 10:
        print(w[0] + str(length - 2) + w[-1])
    else:
        print(w)
