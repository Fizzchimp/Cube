# Recursive binary Searching algorithm
def binSearch(arr, item, front = 0, rear = None):
    if rear == None:
        rear = len(arr) - 1
        
    if rear == -1: 
        return False, None
    
    mid_ptr = (rear + front) // 2
    mid_item = arr[mid_ptr]
    
    # Check if the middle item is the search term
    if mid_item.cube == item.cube:
        return True, mid_item
    
    # Check if the range is 0 (item not in list)
    elif front >= rear:
        return False, None
        
    # Check if the middle item is larger than the search term
    elif mid_item.cube < item.cube:
        return binSearch(arr, item, mid_ptr + 1, rear)
        
    # Check if the middle item is smaller than the search term
    elif mid_item.cube > item.cube:
        return binSearch(arr, item, front, mid_ptr - 1)
    
