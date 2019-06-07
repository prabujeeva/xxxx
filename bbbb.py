a=int(input())
b=a//2
c=0
for x in range(2,b+1):
    if a%x==0:
        c=1 
if c==0:
    print('yes')
else:print('no')
