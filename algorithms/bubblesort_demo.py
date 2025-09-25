import time
import matplotlib.pyplot as plt

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

#visualization
SPEED = 0.03

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Bubble Sort")
    plt.pause(SPEED)

def bubble_sort_viz(arr):
    plt.figure()
    draw(arr)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            draw(arr, (j, j + 1))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                draw(arr, (j, j + 1))
        if not swapped:
            break
    draw(arr)
    plt.show()
    return arr