def insertionsort(a):
  for i in range(len(a)):
    temp = a[i]
    k = i
    while k > 0 and temp < a[k - 1]:
        a[k] = a[k - 1]
        k -= 1
    a[k] = temp

s=input("Enter the numbers")
a=list(map(int, s.split()))
insertionsort(a)
print(a)
