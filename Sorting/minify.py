from math import floor
def minify(a,n,i) :
    smallest=i
    l=(2*i)+1
    r=(2*i)+2
    if (l<n) and (a[l]<a[smallest]) :
        smallest=l
    if (r<n) and (a[r]<a[smallest]) :
        smallest=r
    if smallest!=i :
        a[i],a[smallest]=a[smallest],a[i]
        minify(a,n,smallest)
        
def Build_minheap(a,n):
    for i in range(n,-1,-1):
        minify(a,n,i)
        print("heap",i , a )

def Heapsort():
    s=input("Enter the numbers")
    a=list(map(int, s.split()))
    n=len(a)
    Build_minheap(a,n)
    for i in range(n-1,0,-1):
        a[i],a[0]=a[0],a[i]
        minify(a,i,0)
        print(a)
    print(a)


Heapsort()
#Build_maxheap()
