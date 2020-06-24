# [0 | -2,10]->[-2 | 0, 10] //not last_left
#is last left [-1, -3 | 0]

#in-place: O(1) space
def rearrange(lst): 
    #2nd attempt: 
    #only able to figure it out with example output; next time, don't depend on example output

    #marker for left of delimitation line; keeps track of latest left as "adding" neg- 
    # shifts line forward
    partition_left_idx = 0
    for idx in range(len(lst)):
        if lst[idx] < 0: #if neg-
            #needs this _if_ to reduce the num of unnec- swaps
            if idx is not partition_left_idx: #else, it would just switch with itself
                lst[partition_left_idx], lst[idx] = lst[idx], lst[partition_left_idx] #swap
            #since swap "added" neg- to left, shift delimiter line up one
                #line16 is not at this indent cuz 
                # line needs to move up whether swap happens or not
            partition_left_idx += 1
    
    return lst

#O(n) time
print(rearrange([-1, 2, -3, -4, 5]))
print([-1, -3, -4, 2, 5])
print(rearrange([300, -1, 3, 0]))
print([-1, 300, 3, 0])
print(rearrange([0, 0, 0, -2]))
print([-2, 0, 0, 0])