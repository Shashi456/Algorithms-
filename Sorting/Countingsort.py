#x=int(input("upper bound:"))
#n=int(input("number of elements:"))
s=input("Enter the numbers")
a=list(map(int, s.split()))
n1=max(a)#c[0..n1]
n=len(a)
print(n)
b=[0]*(n)
print("\n")
c=[0]*(n1+1)
for j in a:
    c[j]=c[j]+1
    print(c)
for i in range(1,n1+1):
    c[i]=c[i]+c[i-1]
for i in range(1,n1+1):
    c[i]=c[i]-1    
print(c)
for j in range(n-1,-1,-1):
        b[c[a[j]]]=a[j]
        c[a[j]]=c[a[j]]-1
print(b)
       
    
    
  ##  a comment on the size of b in the book of clrs , although c completely ranges from 0 to k where k is max(a)
  ## b is shown to ranging from 1 to n inclusive , in programming languages c would need to be initialized to -1 and not zero   
  ## or they should be decreased by one as i did . but since would that would add to the complexity of the algorithm it is 
  ## thus advised to not do so. 
