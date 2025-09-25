import time
import matplotlib.pyplot as plt

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

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    import matplotlib.pyplot as plt
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Quick Sort")
    plt.pause(SPEED)

def quick_sort_viz(arr):
    import matplotlib.pyplot as plt
    plt.figure()
    draw(arr)

    def partition_viz(low, high):
        pivot = arr[(low + high) // 2]
        i, j = low, high
        while i <= j:
            while arr[i] < pivot:
                i += 1
                draw(arr, (i, j))
            while arr[j] > pivot:
                j -= 1
                draw(arr, (i, j))
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                draw(arr, (i, j))
                i += 1
                j -= 1
        return i, j

    def sort_viz(low, high):
        if low < high:
            i, j = partition_viz(low, high)
            if low < j:
                sort_viz(low, j)
            if i < high:
                sort_viz(i, high)

    sort_viz(0, len(arr) - 1)
    draw(arr)
    plt.show()
    return arr