l = [-1,5,7,-2,1,0,-1]
k = 5

for i in range(k-1):
    if l[k-1] < l[i]:
        l[k-1], l[i] = l[i], l[k-1]

for i in range(k, len(l)):
    if l[k-1] > l[i]:
        l[k-1], l[i] = l[i], l[k-1]

print(l[k-1])