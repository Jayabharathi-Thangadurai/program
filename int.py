import sys
n,n1 = map(int,sys.stdin.readline().split(' '))
l1=list(map(int,input().split()))
var=0
for i in range(n1):
    var=var+l1[i]
print(var)
