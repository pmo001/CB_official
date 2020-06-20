def findSecondMaximum(lst):
    second_maxVal = float("-inf") #imp: must assign -8 or there will be edge cases that won't be fulfilled
    maxVal = float("-inf")
    #traversing list twice: O(n)
    for j in range(len(lst)):
        if lst[j] > maxVal:
            maxVal = lst[j]
    
    for i in range(len(lst)):
        if lst[i] > second_maxVal and lst[i] < maxVal:
            second_maxVal = lst[i]
            
    return second_maxVal