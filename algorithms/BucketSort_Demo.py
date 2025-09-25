import time
from typing import List
import matplotlib.pyplot as plt

def bucket_sort(arr: List[float]) -> List[float]:
    n = len(arr)
    if n == 0:
        return arr

    start = time.perf_counter()

    buckets = [[] for _ in range(n)]

    for x in arr:
        idx = int(n * x)
        buckets[idx].append(x)

    for i in range(n):
        buckets[i].sort()

    result = []
    for b in buckets:
        result.extend(b)

    end = time.perf_counter()
    print(f"[Bucket] sort of {n} elements in {end - start:.6f} sec")

    return result

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Bucket Sort")
    plt.pause(SPEED)

def bucket_sort_viz(arr):
    plt.figure()
    draw(arr)
    n = len(arr)
    if n == 0:
        plt.show()
        return arr

    buckets = [[] for _ in range(n)]

    # distribute into buckets
    for x in arr:
        idx = int(n * x)
        if idx >= n:      # guard if x==1.0
            idx = n - 1
        buckets[idx].append(x)

    # sort each bucket
    for b in buckets:
        b.sort()

    # concatenate back with placement visualization
    k = 0
    for b in buckets:
        for v in b:
            arr[k] = v
            draw(arr, (k,))
            k += 1

    draw(arr)
    plt.show()
    return arr

