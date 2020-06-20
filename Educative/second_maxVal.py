def findSecondMaximum(lst):
    second_maxVal = float("-inf") #imp: must assign -8 or exist edge cases that won't be fulfilled
    maxVal = float("-inf")

    #traversing list twice: O(n)
    for j in range(len(lst)):
        if lst[j] > maxVal:
            maxVal = lst[j]
    
    for i in range(len(lst)):
        #less correct: lst[i] < maxVal: or lst[i] != maxVal
        #below accounts for more edge cases
            #accounts for duplicate numbers; <is not> makes sure is not the same object as maxVal
        if lst[i] > second_maxVal and lst[i] is not maxVal:
            second_maxVal = lst[i]
            
    return second_maxVal