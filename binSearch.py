def binSearch(arr, item, front = 0, rear = None):
    if rear == None: rear = len(arr) - 1
    mid = (rear + front) // 2
    midItem = arr[mid]
        
    if midItem == item:
        return True
        
    elif front == rear:
        return False
        
    elif midItem < item:
        return binSearch(arr, item, mid + 1, rear)
        
    elif midItem > item:
        return binSearch(arr, item, 0, mid - 1)
