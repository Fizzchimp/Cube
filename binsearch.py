# Recursive binary Searching algorithm
def binSearch(arr, item, front = 0, rear = None):
    if rear == None:
        rear = len(arr) - 1
        
    if rear == -1: 
        return False, None
    
    mid = (rear + front) // 2
    midItem = arr[mid]
    
    # Check if the middle item is the search term
    if midItem.cube == item.cube:
        return True, midItem
    
    # Check if the range is 0 (item not in list)
    elif front >= rear:
        return False, None
        
    # Check if the middle item is larger than the search term
    elif midItem.cube < item.cube:
        return binSearch(arr, item, mid + 1, rear)
        
    # Check if the middle item is smaller than the search term
    elif midItem.cube > item.cube:
        return binSearch(arr, item, front, mid - 1)
    
