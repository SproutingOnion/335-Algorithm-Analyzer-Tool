import time
import matplotlib.pyplot as plt

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

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Insertion Sort")
    plt.pause(SPEED)

def insertion_sort_viz(arr):
    plt.figure()
    draw(arr)
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        draw(arr, (j, i))          # show initial comparison
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]    # shift
            j -= 1
            draw(arr, (j, j + 1))  # show shift positions
        arr[j + 1] = key           # insert key
        draw(arr, (j + 1,))        # show insertion
    draw(arr)
    plt.show()
    return arr
