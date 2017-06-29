def quicksort(a,p,r,count):
    if p<r :
        q = partition(a,p,r,count)
        quicksort(a,p,q-1,count)
        quicksort(a,q+1,r,count)
#so to analyze both the algos i will be counting the number of partitions
def partition(a,p,r,count) :
    
    x=a[r]
    i=p-1
    for j in range(p,r) :
        if a[j]>=x: #change this sign if you want ascending or descending
            count=count+1
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1

#randomized pivot element

from random import randint
def r_partition(b,p,r,countr):
    i=randint(p,r)
    b[r],b[i]=b[i],b[r]
    return rpartition(b,p,r,countr)
def rpartition(a,p,r,countr) :
   
    x=a[r]
    i=p-1
    for j in range(p,r) :
        if a[j]>=x: #change this sign if you want ascending or descending
            countr=countr+1
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1

def r_quicksort(b,p,r,countr):
    if p<r :
        q = r_partition(b,p,r,countr)
        r_quicksort(b,p,q-1,countr)
        r_quicksort(b,q+1,r,countr)


s=input("Enter the numbers")
a=list(map(int, s.split()))
b=a[:]
n=len(a)
count=0
countr=0
quicksort(a,0,n-1,count)
print(a,"count",count)
r_quicksort(b,0,n-1,countr)
print(b,"count",countr)
