#x=int(input("upper bound:"))
#n=int(input("number of elements:"))
s=input("Enter the numbers")
a=list(map(int, s.split()))
n1=max(a)#c[0..n1]
n=len(a)
b=[0 for i in range(n)]
print("\n")
c=[0]*(n1+1)
for j in a:
    c[j]=c[j]+1
    print(c)
##for i in range(1,n1+1):
##    c[i]=c[i]+c[i-1]
##    print(c)
##for j in range(n-1,0,-1):
##    try:
##        b[c[a[j]]]=a[j]
##        c[a[j]]=c[a[j]]-1
##    except:
##        pass
    
print(b)
