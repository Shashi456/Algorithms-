


# Let s be the string
# let r1, r2 = compare(s, i, j)
# return r1=x+1,r2=y+1 for which:
# - precondition(i<j)
# - s[i:x] == s[j:y] 
# - s[x+1] != s[y+1]
def compare(s, i, j):
    #assert(i<j)
    while(i<len(s) and j<len(s)):
        if(s[i] == s[j]):
            i = i + 1 
            j = j + 1 
        else:
            return i, j 
    # if(j>=len(s)):
    return i, j 

    #raise RuntimeError("You didn't think of this case")

# Z Algo Psedo-code
# r, l = ?
# k = ?
# if k>r 
#  z = Compare(S[k], S[1])
#  Z[k] = z
#  r = k + Z[k] - 1
#  l = k
# else
#  k' = k - l + 1
#  B = r - k + 1 
#   if Z[k'] < B
#     Z[k] = Z[k']
#   else 
#     z = Compare(S[r+1], s[B+1])
#     Z[k] = z - k
#     r = q - 1 
#     l = k 



def Zalgo(s):
    Z = [0] * len(s) 
    r = 0 
    l = 0 
    k = 1
    for k in range(1, len(s)):
        if k > r:
            r1, r2 = compare(s, 0, k)
            Z[k] = r2 - k 
            r = k + Z[k] - 1
            l = k 
        else:
            k1 = k - l + 1 
            B = r - k + 1
            if Z[k1] < B :
                Z[k] = Z[k1]
            else :
                r1, r2 = compare(s, r+1, B+1)
                Z[k] = r2 - k 
                r = r2 - 1
                l = k
    return Z 
#s = "abcabcabc"
s = "aabcaabxaaz"
z = Zalgo(s)
print("String:", s)
print("Z-Box array:", z)

                


    

