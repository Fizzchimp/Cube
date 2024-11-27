# Recursive merge sorting algorithm
def merge_sort(arr):
    if len(arr) > 1:
        # Break the list down into smaller pieces
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
    
        # Merge the two ordered lists
        lPnt = rPnt = i = 0
        while True:
            try:
                lItem = left[lPnt]
            except IndexError:
                arr[i:] = right[rPnt:]
                break
            
            try:
                rItem = right[rPnt]
            except IndexError:
                arr[i:] = left[lPnt:]
                break
      
            if lItem.cube <= rItem.cube:
                arr[i] = lItem
                lPnt += 1
                
            elif rItem.cube <= lItem.cube:
                arr[i] = rItem
                rPnt += 1
        
            i += 1
            
    return arr
