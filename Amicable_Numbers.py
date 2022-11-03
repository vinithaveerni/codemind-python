n=int(input())
v=int(input())
s=0
c=0
for i in range(1,n):
    if n%i==0:
        s+=i
for j in range(1,v):
    if v%j==0:
        c+=j
if s==v and c==n:
    print("Amicable")
else:
    print("Not Amicable")