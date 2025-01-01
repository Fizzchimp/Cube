# Recursive binary Searching algorithm
def bin_search(arr, item, front = 0, rear = None):

    # Rear points to end of current searching list
    if rear == None:
        rear = len(arr) - 1
        
    if rear == -1: 
        return False, None
    
    # Points to middle of list
    mid_ptr = (rear + front) // 2
    mid_item = arr[mid_ptr]
    
    # Check if middle item is equal to search term
    if mid_item.cube == item.cube:
        return True, mid_item
    
    # Check if the range is 0 (item not in list)
    elif front >= rear:
        return False, None
        
    # Check if middle item is larger than the search term
    elif mid_item.cube < item.cube:
        return bin_search(arr, item, mid_ptr + 1, rear)
        
    # Check if middle item is smaller than the search term
    elif mid_item.cube > item.cube:
        return bin_search(arr, item, front, mid_ptr - 1)

