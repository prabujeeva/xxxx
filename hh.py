x=int(input())
y=[]
for j in range(0,x):  
    z=input()
    y.append(z)
list=[]
for j in zip(*y):
    if j.count(j[0])==len(j): 
        list.append(j[0])
    else:
        break
print(''.join(list))
