n=int(input())
t=n
i=0
while n>0:
    r=n%10
    i=i*10+r
    n=n//10
if t==i:
    print("True")
else:
    print("False")