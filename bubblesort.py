n=int(input("Number of items :"))
l=[]
count=0
counti=0
for i in range(0,n):
    a=int(input())
    l.append(a)
l1=l[:]
for i in range(0,n):
    for j in range(1,n):
        count=count+1
        if(l[j-1]>l[j]):
            l[j-1],l[j]=l[j],l[j-1]
print(l)
print("count :",count)
        
        
    
