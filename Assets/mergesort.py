# Recursive merge sorting algorithm
def merge_sort(arr):
    # Check if final recursion depth is reached (only one item in list)
    if len(arr) > 1:

        # Breaks list down into two halves and calls function again for both halves
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
    

        # Merge the two ordered lists

        lPnt = rPnt = i = 0
        while True:
            try:
                # Set lItem to next item in list to be compared
                lItem = left[lPnt]
            except IndexError:
                # If no more items in left list, add the rest of the right list to the sorted list
                arr[i:] = right[rPnt:]
                break
            
            try:
                # Set rItem to next item in list to be compared
                rItem = right[rPnt]
            except IndexError:
                # If no more items in right list, add the rest of the left list to the sorted list
                arr[i:] = left[lPnt:]
                break
      
            if lItem.cube <= rItem.cube:
                # If the left item is smaller than the right, add the left item to the sorted list
                arr[i] = lItem
                # Increment left pointer to next item to be compared
                lPnt += 1
                
            elif rItem.cube <= lItem.cube:
                # If the right item is smaller than the left, add the right item to the sorted list
                arr[i] = rItem
                # Incrmeent left pointer to next item to be compared
                rPnt += 1
        
            # Increment the position pointer of the sorted list
            i += 1
            
    return arr
