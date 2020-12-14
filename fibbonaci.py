n=int(input())
f=0
s=1
temp=0
print(1)
for i in range(n):
    temp=s
    s=s+f
    f=temp
    print(s)
