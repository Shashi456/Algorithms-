def quicksort(a,p,r):
    if p<r :
        q = partition(a,p,r)
        quicksort(a,p,q-1)
        quicksort(a,q+1,r)
def partition(a,p,r) :
    x=a[r]
    i=p-1
    for j in range(p,r) :
        if a[j]>=x: #change this sign if you want ascending or descending
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1

s=input("Enter the numbers")
a=list(map(int, s.split()))
n=len(a)
quicksort(a,0,n-1)
print(a)
