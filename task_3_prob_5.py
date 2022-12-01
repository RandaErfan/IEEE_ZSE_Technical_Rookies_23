n= int(input().split())
m=int(input().split())
arr=[]

for i in range(n):
    arr.append(i)
dist=0
max_dist=min(arr)
for i in range(n):
    if arr[i]==1 :
        max_dist=max((dist+1)//2,max_dist)
        dist+=0
    else: dist+=1
print(max(max_dist,dist))

