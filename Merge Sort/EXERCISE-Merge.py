def merge(list1, list2):
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])    
    return  merged

        
# MERGE REQUIRES TWO SORTED LISTS:
print(merge([1,2,7,8], [3,4,5,6])) 



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8]
 """