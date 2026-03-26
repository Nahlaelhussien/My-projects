n,m = map(int,input().split())
a= list(map(int,input().split()))
b=list(map(int,input().split()))
i = 0
result = []
    
for x in b:
    while i < n and a[i] < x:
        i += 1
    result.append(i)
    
print(*result)
