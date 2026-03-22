t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    l.sort()
    for j in range(n-1):
        if l[j]<=l[j+1] and abs(l[j]-l[j+1])<=1:
            count+=1
    if n-count==1:
        print("Yes")
    else:
        print("No")
