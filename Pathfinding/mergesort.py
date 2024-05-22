# Recursive merge sorting algorithm
def mergeSort(list):
    if len(list) > 1:
        # Break the list down into smaller pieces
        left = mergeSort(list[:len(list) // 2])
        right = mergeSort(list[len(list) // 2:])
    
        # Merge the two ordered lists
        lPnt = rPnt = i = 0
        while True:
            try:
                lItem = left[lPnt]
            except IndexError:
                list[i:] = right[rPnt:]
                break
            
            try:
                rItem = right[rPnt]
            except IndexError:
                list[i:] = left[lPnt:]
                break
      
            if lItem.cube <= rItem.cube:
                list[i] = lItem
                lPnt += 1
                
            elif rItem.cube <= lItem.cube:
                list[i] = rItem
                rPnt += 1
        
            i += 1
            
    return list
