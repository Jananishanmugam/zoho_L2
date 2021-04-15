a = input()
n = len(a)
mid = len(a)//2
j = len(a)-1
for i in range(mid,n):
    print(' '*j,end='')
    print(a[mid:i+1])
    j=j-1
 
for i in range(1,mid+1):
    print(' '*j,end='')
    j=j-1
    print(a[mid:]+a[0:i])
    


