def findFirstUnique(lst):
    ordereddict = dict()
    for i in range(len(lst)):
        if lst[i] not in ordereddict:
            ordereddict[lst[i]] = 1
        else:
            ordereddict[lst[i]] += 1
    
    for key in ordereddict:
        if ordereddict[key] == 1:
            return key

print(findFirstUnique([4, 5, 1, 2, 0, 4]))