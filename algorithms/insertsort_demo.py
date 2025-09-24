import time

def insertion_sort(arr):
    start = time.perf_counter()
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key: # shiftselements that are greater than key value
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    end = time.perf_counter()
    print(f"[Insert] sort in {end-start:.6f} sec.")    
    return arr


