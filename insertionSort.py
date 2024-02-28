#The code performs insertion sort at which sorted element inserted into another list


# a =[2,6,4,5,1,3,7,2,3,4,10]
# b = []
# for i in a:
#     if len(b) ==0:
#         b.append(i)
#     elif len(b)==1:
#         if i> b[0]:
#             b.append(i)
#         else:
#             b.insert(0,i)
#         # print(b)

#     else:
#         for j in range(0,len(b)-1):
#             if b[j]<=i and b[j+1]>i:
#                 b.insert(j+1,i)
#                 # print(b)
#                 break 
#             elif b[0]>=i:
#                 b.insert(0,i)
#                 # print(b)
                
#                 break 
#             elif b[len(b)-1]<=i:
#                 b.append(i)
#                 break           
# print(b)
#The code for insertion sort into a single list .
a =[2,6,4,5,1,3,7,2,3,4,10]

for i in range(1,len(a)):
    val = a[i]
    hl = i
    while hl>0 and val< a[hl-1]:
        a[hl]=a[hl-1]
        hl = hl -1
    a[hl] = val
print(a)