import time
def quick_sort(arr):
    start = time.perf_counter()
    def partition(low, high):
        pivot = arr [(low + high) // 2]
        i = low
        j = high
        while i <= j:
            while arr[i] < pivot:
                i += 1 
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return i, j
    def sort(low, high):
        if low < high:
            i, j = partition(low, high)
            sort(low, j)
            sort(i, high)
    sort(0, len(arr) - 1)
    end = time.perf_counter()
    print(f"[Quick] sort in {end - start:.6f} sec.")
    return arr


