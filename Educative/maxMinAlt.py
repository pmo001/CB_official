def maxMin(lst): #lst is already sorted
    #max first then min; alternating
    newList = []
    end = len(lst) - 1
    begin = 0 #don't really need this

    for i in range(len(lst) // 2): #go halfway to midpt
        #imp: add both at same time
        #even idx == max
        newList.append(lst[end - i])
        newList.append(lst[begin + i]) #don't need the begin
    
    midpt_floor = len(lst) // 2
    if len(lst) % 2 == 1: #if odd len(), then add the midpt to end of list
        newList.append(lst[midpt_floor])

    return newList