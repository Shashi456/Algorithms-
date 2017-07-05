def countingsort(a,n,exp):
    n=len(a)
    b=[0]*(n)
    c=[0]*(10)
    
    for j in a:
        c[int(j/exp)%10]=c[int(j/exp)%10]+1
    for i in range(1,10):
        c[i]=c[i]+c[i-1]
    for i in range(10):
        c[i]=c[i]-1    
    for j in range(n-1,-1,-1):
            b[c[int(a[j]/exp)%10]]=a[j]
            c[int(a[j]/exp)%10]=c[int(a[j]/exp)%10]-1
    return b


s=input("Enter the numbers")
a=list(map(int, s.split()))
#b=[[0,i] for i in a ]
x=max(a)
exp=1
n=0
while (x/exp)>0:
    a=countingsort(a,n,exp)
    exp=exp*10
print(a)
    
