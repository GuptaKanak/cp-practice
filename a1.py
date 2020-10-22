#Function to replace each element of the array with product of every other element without using division operator
def replace(a,left,i):
  if i==len(a):return 1 
  temp=a[i]
  right=replace(a,left*a[i],i+1)
  a[i]=left*right
  return temp*right
array=list(map(int,input().split()))
replace(array,1,0)
print(*array)
#input= 1 2 3 4 5
#output=120 60 40 30 24
#
