def relativeSortArray(arr1, arr2):
    newTab = []
    rest = arr1.copy()
    for i in arr2:
        j = 0
        for j in arr1:
            if j == i:
                newTab.append(i)
                rest.remove(j)
    l = 0
    while l < len(rest)-1:
        if rest[l] > rest[l+1]:
            tmp = rest[l]
            rest[l] = rest[l+1]
            rest[l+1] = tmp
            l = 0
        else :
            l += 1
    return newTab + rest

print (relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
# Output: [2,2,2,1,4,3,3,9,6,7,19]
print (relativeSortArray([28,6,22,8,44,17], [22,28,8,6]))
# Output: [22,28,8,6,17,44]
print(relativeSortArray([2,3,1,3,2,4,6,19,9,2,7],[2,1,4,3,9,6])) 
# [2,2,2,1,4,3,3,9,6,7,19]
print(relativeSortArray([26,21,11,20,50,34,1,18], [21,11,26,20]))
# [21,11,26,20,1,18,34,50]