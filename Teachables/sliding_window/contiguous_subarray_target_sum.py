#[ 1,2,3,3,3] 
#^ window begin

def sliding_window(arr, target):
    window_begin_exclu = -1 #out of bounds
    window_sum = 0
    num_subarrays = 0
    for window_end_inclu in range(len(arr)):
        
    #0 - -1 == 1
    #1 -  0 == 1 #if 5 was skipped, and 4 hit target 
    # [ 1,2,3,3,3] : [1],[2], [1,2],[3]*3 == 3 + 3 = 6
    #begin: 2,3,4: 4--1=5
    # [1,2,3,0,3] : [1][2][3][0][3][12][30][03] = 8
    #begin:  4 -- 3 == 7
        window_sum += arr[window_end_inclu]

        #[1,2] wb:exclu at -1
        #[1,2,3], need to move window to _idx1_
        #sum at 6, while sum still > target, keep removing left of window
        #window[2,3] wb:exclu at -1+1 ==0
        #window[3] wb:exclu at          0+1=1 =>desired
        while window_sum > target: #[5, 4, ...] => move window to 4
            #don't want 5, so move window to 5 since exclu
            window_begin_exclu += 1 #now at idx0
            window_sum -= arr[ window_begin_exclu ]

        num_subarrays += window_end_inclu - window_begin_exclu 
                        #0 - - 1 ==1 #keeping idx0
                        #1 -   0 ==1 #skipping5, keeping3 [5,3...0,2]
                        #assume 0 at idx3: 4 - 2(since window at id2(exclu)) = 2
                        #hence why += instead of plain =
        #print(num_subarrays)
    return num_subarrays

arr1 = [1,2,3,0,3]
print(">>>>>>>>")
print(sliding_window(arr1, 3))
print("answer should be 8")

arr2 = [5,3,6,0,2]
print(sliding_window(arr2, 3), "4 is the answer")

arr3 = [1,2,3,3,3] 
print(sliding_window(arr3, 3), "6 is the answer")




