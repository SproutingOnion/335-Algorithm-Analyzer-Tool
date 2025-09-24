import time

def bubble_sort(arr): 
    start = time.perf_counter()           #defining a bubble sort fn that takes a list as an input
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    end = time.perf_counter()
    print(f"[Bubble] sort in {end - start:.6f} sec.")    
    return arr

