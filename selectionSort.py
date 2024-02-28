# a =[2,7,4,1,5,3]
a =[2,6,4,5,1,3,7,2,3,4,10]

for i in range(0,len(a)):
    iMin =i
    for j in range(i+1,len(a)):
        if a[iMin]>a[j]:
            iMin = j
    a[iMin],a[i] = a[i],a[iMin]
print(a)