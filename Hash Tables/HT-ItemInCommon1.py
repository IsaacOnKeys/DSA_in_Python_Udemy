def item_in_common(list1, list2):

    hashMap = {}  # number : True

    for i in list1:
        if i not in hashMap:
            hashMap[i] = True

    for i in list2:
        if i in hashMap:
            return True
    else:
        return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))
