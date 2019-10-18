l = [1,2,2,2,2,2,2,2,2,2,11]
val = 1

# recursive implementation
def binarysearch(beg=0, end=len(l)-1):
    if beg > end:
        return 'Not found'
    mid = (beg + end)//2
    if l[mid] == val:
        return 'Found in index {}'.format(mid)
    elif val > l[mid]:
        beg = mid + 1
        return binarysearch(beg, end)
    else:
        end = mid - 1
        return binarysearch(beg, end)


print(binarysearch())


# iterative implementation

def binarysearchiter(beg=0, end=len(l)-1):
    while beg <= end:
        mid = (beg+end)//2

        if l[mid] == val:
            return "Found at " + str(mid)
        elif val > l[mid]:
            beg = mid+1
        else:
            end = mid-1

    return "Not found"

print(binarysearchiter())

# search leftmost index

def binarysearchiterleft(beg=0, end=len(l)-1):
    rslt = -1
    while(beg <= end):
        mid = (beg+end)//2
        if l[mid] == val:
            rslt = mid
            end = rslt - 1
        elif val < l[mid]:
            end = mid - 1
        else:
            beg = mid + 1

    return "Found at " + str(rslt) if rslt >= 0 else "Not Found"

print(binarysearchiterleft())

# search rightmost index
rslt = -1
def binarysearchright(beg=0, end=len(l)-1):
    if beg > end:
        global rslt
        return "Found at " + str(rslt) if rslt >= 0 else 'Not Found'
    mid = (beg+end)//2
    if val == l[mid]:
        rslt = mid
        return binarysearchright(mid+1, end)
    elif val > l[mid]:
        return binarysearchright(mid+1, end)
    else:
        return binarysearchright(beg, mid-1)

print(binarysearchright())

# find count of a number in a sorted list

def findCount(l, key):
    firstIndex = binarysearchoccurence(l, key, True)
    lastIndex = binarysearchoccurence(l, key, False)
    if firstIndex == -1 or lastIndex == -1:
        return 0
    return (lastIndex-firstIndex)+1


def binarysearchoccurence(l, key, isFirst):
    beg = 0
    end = len(l)-1
    index = -1
    while beg <= end:
        mid = (beg+end)//2
        if key == l[mid]:
            index = mid
            if isFirst:
                end = mid-1
            else:
                beg = mid+1
        elif key > l[mid]:
            beg = mid+1
        else:
            end = mid-1

    return index


print(findCount([1,2,3,4,5,5,6,6,6,6,6,6,6,6,6,9],9))

# how many times is a circular sorted array rotated(all elements must be unique)

def totalRotations(l):
    beg = 0
    end = len(l)-1
    while beg <= end:
        if l[beg] <= l[end]:
            return beg
        mid = (beg+end)//2
        if l[mid-1] > l[mid] < l[mid+1]:
            return mid
        elif l[mid] < l[end]:
            end = mid-1
        else:
            beg = mid+1

print(totalRotations([8,9,10,11,12,13,14,15,16,1,2,3,4,5,6,7]))

# find element in a circularly sorted array with distinct elements

def findElt(l, k):
    beg = 0
    end = len(l)-1
    while(beg <= end):
        mid = (beg+end)//2
        if k == l[mid]:
            return mid;
        if l[mid] <= l[end]:   # right half is sorted
            if l[end] >= k > l[mid]:
                beg = mid + 1
            else:
                end = mid - 1
        else: # left half is sorted
            if l[beg] <= k < l[mid]:
                end = mid - 1
            else:
                beg = mid + 1

    return 'Not found'


print(findElt([3,5,6,7,8,9,1,2,3],19))