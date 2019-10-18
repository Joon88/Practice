l = [1,2,3,4,5]

left = [1]*len(l)
right = [1]*len(l)
ans = list()
for i in range(1, len(l)):
    left[i] = left[i-1]*l[i-1]

for i in range(len(l) - 2, -1, -1):
    right[i] = right[i+1]*l[i+1]

for i in range(len(l)):
    ans.append(left[i]*right[i])

print(ans)