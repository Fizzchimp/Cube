# Recursive merge sorting algorithm
def merge_sort(arr):
    # Check if final recursion depth is reached (only one item in list)
    if len(arr) > 1:

        # Breaks list down into two halves and calls function again for both halves
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
    

        # Merge the two ordered lists

        left_ptr = right_ptr = i = 0
        while True:
            try:
                # Set left_item to next item in list to be compared
                left_item = left[left_ptr]
            except IndexError:
                # If no more items in left list, add the rest of the right list to the sorted list
                arr[i:] = right[right_ptr:]
                break
            
            try:
                # Set right_item to next item in list to be compared
                right_item = right[right_ptr]
            except IndexError:
                # If no more items in right list, add the rest of the left list to the sorted list
                arr[i:] = left[left_ptr:]
                break
      
            if left_item.cube <= right_item.cube:
                # If the left item is smaller than the right, add the left item to the sorted list
                arr[i] = left_item
                # Increment left pointer to next item to be compared
                left_ptr += 1
                
            elif right_item.cube <= left_item.cube:
                # If the right item is smaller than the left, add the right item to the sorted list
                arr[i] = right_item
                # Increment left pointer to next item to be compared
                right_ptr += 1
        
            # Increment the position pointer of the sorted list
            i += 1
            
    return arr
