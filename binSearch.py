def binSearch(arr, item, front = 0, rear = None):
    if rear == None: rear = len(arr) - 1
    mid = (rear + front) // 2
    midItem = arr[mid]
    
    if midItem == item:
        print(f"Found at pos {mid}")
        return
    
    elif front == rear:
        print("Not found. Inserting.")
        #if midItem > item: list.insert(mid, item)
        arr.insert(mid if midItem > item else mid + 1, item)
        return
    
    elif midItem < item:
        return binSearch(arr, item, mid + 1, rear)
    
    elif midItem > item:
        return binSearch(arr, item, 0, mid - 1)


arr1 = [0]

for i in range(1000):
    binSearch(arr1, 1000 - i)
print(arr1)
