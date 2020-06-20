#in-place: O(1) space
def rearrange(lst): # [0 | -2,10]->[-2 | 0, 10] //not last_left
#is last left [-1, -3 | 0]
#marker for left of delimitation line; keeps track of latest left as adding neg. shifts line forward
    last_left = 0
    for idx in range(len(lst)):
        if lst[idx] < 0: #if neg.
            if idx is not last_left: #else, it would just switch with itself
                lst[last_left], lst[idx] = lst[idx], lst[last_left] #swap
            #since swap added neg. to left, shift delimiter line up one
            last_left += 1
    
    return lst

#O(n) time
print(rearrange([-1, 2, -3, -4, 5]))
print(rearrange([300, -1, 3, 0]))
print(rearrange([0, 0, 0, -2]))