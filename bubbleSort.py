a =[2,6,4,5,1,3,7,2,3,4,10]
for _ in (a):
    for i in range(0,len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            
print(a)