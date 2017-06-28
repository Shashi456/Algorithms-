from math import floor
def Maxify(a,n,i) :
    largest=i
    l=(2*i)+1
    r=(2*i)+2
    if (l<n) and (a[l]>a[largest]) :
        largest=l
    if (r<n) and (a[r]>a[largest]) :
        largest=r
    if largest!=i :
        a[i],a[largest]=a[largest],a[i]
        Maxify(a,n,largest)
        
def Build_maxheap(a,n):
    for i in range(n,-1,-1):
        Maxify(a,n,i)
        #print("heap",i , a )

def Heapsort():
    s=input("Enter the numbers")
    a=list(map(int, s.split()))
    n=len(a)
    Build_maxheap(a,n)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        Maxify(a,i,0)
        #print(a)
    print(a)


Heapsort()


