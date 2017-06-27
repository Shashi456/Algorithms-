from math import floor
def Maxify(a,i) :
    l=(2*i)+1
    r=(2*i)+2
    size=len(a)
    if (l<=size) and (a[l]>a[i]) :
        largest=l
    else :
        largest=i
    if (r<=size) and (a[r]>a[largest]) :
        largest=r
    if largest!=i :
        a[i],a[largest]=a[largest],a[i]
        Maxify(a,largest)
        
def Build_maxheap():
    s=int(input("No:"))
    a=[]
    for i in range(0,s):
        x=input()
        a.append(x)
    size=len(a)
    for i in range(floor((size/2)-1),-1,-1):
        print(i)
        Maxify(a,i)
        print(a)

"""def Heapsort():
    a=list(input("Enter a list of numbers: "))
    Build_maxheap(a)
    for i in range(len(a)-1,0,-1):
        a[0],a[i]=a[i],a[0]
        Maxify(a,0)
    print(a)


Heapsort()"""
Build_maxheap()
