'''
#567891234
def bs(a,l,r):
    if l<r:
        m=(l+r)//2
        if a[m-1]>=a[m]<=a[m+1]:return m
        elif a[m]<=a[l]:return bs(a,l,m-1)
        elif a[m]>=a[r]:return bs(a,m+1,r)

#====search for the element in circularlly anticlockwise rotated aaray
def csbs(a,l,r,x):
    if l<r:
        m=(l+r)//2
        if a[m]==x:return m
        elif a[m]<=a[r]:
            if x>a[m] and x<=a[r]:return csbs(a,mid+1,r,x)
            else:csbs(a,l,mid-1,x)
        elif a[m]>=a[l]:
            if x<a[m] and x>=a[l]:return csbs(a,l,mid-1,x)
            else:csbs(a,mid+1,r,x)
a=list(map(int,input().split()))
x=int(input())
print(csbs(a,0,len(a)-1,x))
#=====repetitive count
def rbs(a,l,r,x,f,result=-1):
    if l<r:
        m=(l+r)//2
        if a[m]==x:
            result=m
            if f:l=m-1
            else:l=m+1
'''
# Find all binary strings that can be formed from given wildcard pattern
def p(s,i=0):
    if i==len(s):
        print(s)
        return 
    if s[i]=='?':
        for c in '01':
            s[i]=c
            p(s,i+1)
            s[i]='?'
    else:p(list(s),i+1)
def bv(n,s):
    p=s
    if n==0:
        print(s)
        return
    for c in '01':
        p+=c
        bv(n-1,p)
        p=s

keypad = [
        # 0 and 1 digit don't have any characters associated
        [''],
        ['A', 'B', 'C'],
        ['D', 'E', 'F'],
        ['G', 'H', 'I'],
        ['J', 'K', 'L'],
        ['M', 'N', 'O'],
        ['P', 'Q', 'R', 'S'],
        ['T', 'U', 'V'],
        ['W', 'X', 'Y', 'Z']
    ]
def mp(l,res,n):
    p=res
    if n==len(l):
        print(p)
        return
    for i in keypad[l[n]]:
        p+=i
        mp(l,p,n+1)
        p=res
l=list(map(int,input().split()))
mp(l,'',0)
