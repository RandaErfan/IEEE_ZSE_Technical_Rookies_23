from tkinter.messagebox import YES


n=int(input("number of botteles :"))
arr=[]
for i in range(n):
    v= input().split()
    arr.append(v)
print (arr)
vol=0
cap=0
for i in range(n):
    for j in range(n):
        vol+=arr[j][0]
        cap+=arr[j][1]
if (vol%2 == 0)and (vol <= cap):
    print("YES")
else:
    print("NO")

