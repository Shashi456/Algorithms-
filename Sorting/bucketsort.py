def insertionsort(a):
  for i in range(len(a)):
    temp = a[i]
    k = i
    while k > 0 and temp < a[k - 1]:
        a[k] = a[k - 1]
        k -= 1
    a[k] = temp

def bucketsort(a):
    b=[]
    n=len(a)
    for i in range(1,11):
        l=[]
        b.append(l)
    x=max(a)
    d=0.1

    while x>0:
        x=int(x/10)
        d=d*10
        
    for i in range(n):
        j=int(a[i]/d)
        print(j)
        b[j].append(a[i])

    for i in range(1,11):
        try:
            insertionsort(b[i])
        except:
            pass
    l=[]    
    for i in b :
        for j in i :
            l.append(j)
    print(l)
                
s = input("Enter the numbers")
a=list(map(int, s.split()))
bucketsort(a)
