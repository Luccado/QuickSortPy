def quicksort(array, left, right):
    if left < right:
        partition_pos = partition(array, left, right)
        quicksort(array, left, partition_pos - 1)
        quicksort(array, partition_pos + 1, right)
        

def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]
    
    while i < j:
        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        
        if i < j:
            array[i], array[j] = array[j], array[i]
    
    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]
        
    return i

input_str = input("Elementos da array: ")
arr = [int(x) for x in input_str.split(',')]

quicksort(arr, 0, len(arr) - 1)
print("Array ordenado:", arr)