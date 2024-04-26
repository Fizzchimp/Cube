import random

def mergeSort(list):
  print(list)
  if len(list) > 1:
    left = list[:len(list) // 2]
    right = list[len(list) // 2:]
    mergeSort(left)
    mergeSort(right)
  
    i = j = k = 0
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        list[k] = left[i]
        i += 1
      else:
        list[k] = right[j]
        j += 1
      k += 1
    
    while i < len(left):
      list[k] = left[i]
      k += 1
      i += 1
    while j < len(left):
      list[k] = right[j]
      k += 1
      j += 1
  return list

def mergeSort(list):
  if len(list) > 1:
    left = list[:len(list) // 2]
    right = list[len(list) // 2:]
    print(left, right)
    mergeSort(left)
    mergeSort(right)
    
    i = j = 0
    while i < len(left) or j < len(right):
  
a    rr = [random.randint(1, 100) for i in range(11)]
print(arr)


print(mergeSort(arr))