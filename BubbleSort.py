l = [9,5,1,4,7,8,6,3,2]

for i in range(len(l)):
    for j in range(1,len(l)-i):
        if l[j-1] > l[j]:
            l[j-1], l[j] = l[j], l[j-1]

print(l)