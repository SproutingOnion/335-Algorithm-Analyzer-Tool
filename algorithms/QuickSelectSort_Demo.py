import time
from typing import List
import matplotlib.pyplot as plt

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_select(arr: List[int], low: int, high: int, k: int) -> int:
    # recursive quick select

    if low <= high:
        pi = partition(arr, low, high)
        if pi == k:
            return arr[pi]
    elif pi > k:
        return quick_select(arr, low, pi - 1, k)
    else:
        return quick_select(arr, pi + 1, high, k)


def timed_quick_select(arr: List[int], k: int) -> int:
    start = time.perf_counter()
    result = quick_select(arr, 0, len(arr) - 1, k)
    end = time.perf_counter()
    print(f"[QuickSelect] found k={k} in {end - start:.6f} sec")
    return result

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Quick Select")
    plt.pause(SPEED)

def quick_select_viz(arr, k):
    # k is 0-based index (0..len(arr)-1)
    if not arr or k < 0 or k >= len(arr):
        return None
    plt.figure()
    draw(arr)

    low, high = 0, len(arr) - 1
    while low <= high:
        pivot = arr[high]
        i = low
        draw(arr, (high,))                 # show pivot
        for j in range(low, high):
            draw(arr, (j, high))           # compare with pivot
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                draw(arr, (i, j))          # show swap
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        draw(arr, (i,))                    # pivot placed

        if k == i:
            draw(arr, (i,))
            plt.show()
            return arr[i]
        elif k < i:
            high = i - 1
        else:
            low = i + 1

    plt.show()
    return None
