n,m=map(int,input().split())
l1=[]
for k in range(n,m):
    if k%2!=0 and k!=1:
        l1.append(k)
print(*l1)
