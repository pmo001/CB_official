def rightRotate(lst, n):
    #IMP: RIGHT TO LEFT
    #n == n'th element to be included in rotation
    #O(n)
    #add to new list: space: O(n)
    newList = []
    newList = lst[-n:] + lst[: len(lst) - n]
    return newList

print(rightRotate([10, 20, 30, 40, 50], abs(3)))