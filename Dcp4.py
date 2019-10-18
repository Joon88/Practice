l = [2,-1,0]


def giveLeastNumber():
    for i in range(len(l)):
        if l[i] < 0 or l[i] > len(l):
            l[i] = 0
    #print(l)
    for i in range(len(l)):
        if abs(l[i]) > 0:
            x = abs(l[i]) - 1
            l[x] *= -1
    #print(l)
    for i in range(len(l)):
        if l[i] > 0:
            return i+1

    return min(l)*(-1)+1


print(giveLeastNumber())

'''
3 4 0 1   - all -ves to zero

3 4 0 1   - always negate l[i]-1 index

3 4 0 -1   - if l[i] = 0 skip

-3 4 0 -1  - always consider mod of l[i]
'''


