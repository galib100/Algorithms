def MergeTwoList(l,r,a):
    nL = len(l)
    nR = len(r)
    i =0
    j =0
    k =0
    while(i<nL and j<nR):
        if l[i]<=r[j]:
            a[k] = l[i]
            k+=1
            i+=1
        else:
            a[k]=r[j]
            k+=1
            j+=1
    while(i<nL):
        a[k]=l[i]
        k+=1
        i+=1
    while(j<nR):
        a[k]=r[j]
        k+=1
        j+=1
    # print(a)

a = [2,4,9,10,1,14,10,11,15,13,6,8,5,3,7]
# l  = [1,2,4,6,9,10]
# r  = [3,5,7,8]
# MergeTwoList(l,r,a)
def MergeSort(ar):
    n =len(ar)
    if n<2:
        return n
    mid  =int(n/2)
    
    left = ar[0:mid]
    right =ar[mid:]
    # print(left,right)
    MergeSort(left)
    MergeSort(right)
    MergeTwoList(left,right,ar)
MergeSort(a)
print(a)