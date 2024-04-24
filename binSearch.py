#def binSearch(arr, item, front = 0, rear = None):
#    if rear == None: rear = len(arr) - 1
#    mid = (rear + front) // 2
#    midItem = arr[mid]
#        
#    if midItem == item:
#        print(f"Found at pos {mid}")
#        return
#        
#    elif front == rear:
#        print("Not found. Inserting.")
#        arr.insert(mid if midItem > item else mid + 1, item)
#        return
#        
#    elif midItem < item:
#        return binSearch(arr, item, mid + 1, rear)
#        
#    elif midItem > item:
#        return binSearch(arr, item, 0, mid - 1)


def binSearch(arr, item):
    mid = len(arr) // 2
    print(mid)
    midItem = arr[mid]
        
    if midItem == item:
        return True
        
    elif len(arr) == 1:
        return False
        
    elif midItem < item:
        return binSearch(arr[:mid + 1], item)
        
    elif midItem > item:
        return binSearch(arr[mid:], item)


arr1 = [i for i in range(10)]
print()
