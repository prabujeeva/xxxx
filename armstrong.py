num=int(input())
temp=num
sum=0
while temp>0:
  d=temp%10
  sum=sum+(d**3)
  temp=temp//10
if(num==sum):
  print("yes")
else:
  print("no")
