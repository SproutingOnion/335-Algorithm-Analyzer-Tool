import time
import matplotlib.pyplot as plt

def counting_sort(arr):
    start = time.perf_counter()
    if not arr:
        return []
    max_val = max(arr)
    min_val = min(arr)
    #offset = -min_val if min_val < 0 else 0

    k = max_val - min_val + 1

    count = [0] * k
    for num in arr:
        count[num - min_val] += 1
    output = []
    for i, freq in enumerate(count):
        value = i + min_val
        output.extend([value] * freq)
    end = time.perf_counter()
    print(f"[Counting] sort in {end-start:.6f} sec.")
    return output

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Counting Sort")
    plt.pause(SPEED)

def counting_sort_viz(arr):
    plt.figure()
    draw(arr)
    if not arr:
        plt.show()
        return arr

    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
    count = [0] * k
    for num in arr:
        count[num - min_val] += 1
    for i in range(1, k):
        count[i] += count[i - 1]

    res = [0] * len(arr)
    for num in reversed(arr):
        idx = num - min_val
        count[idx] -= 1
        pos = count[idx]
        res[pos] = num
        draw(res, (pos,))  # show placement

    arr[:] = res
    draw(arr)
    plt.show()
    return arr