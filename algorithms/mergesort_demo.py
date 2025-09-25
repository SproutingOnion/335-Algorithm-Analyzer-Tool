import matplotlib.pyplot as plt

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Merge Sort")
    plt.pause(SPEED)

def merge_sort_viz(arr):
    plt.figure()
    draw(arr)
    n = len(arr)
    temp = [0] * n

    def merge(lo, mid, hi):
        # read from temp, write into arr
        temp[lo:hi + 1] = arr[lo:hi + 1]
        i, j, k = lo, mid + 1, lo
        while i <= mid and j <= hi:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                draw(arr, (k,))
                i += 1
            else:
                arr[k] = temp[j]
                draw(arr, (k,))
                j += 1
            k += 1
        while i <= mid:
            arr[k] = temp[i]
            draw(arr, (k,))
            i += 1
            k += 1
        while j <= hi:
            arr[k] = temp[j]
            draw(arr, (k,))
            j += 1
            k += 1

    def sort(lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        sort(mid + 1, hi)
        merge(lo, mid, hi)

    if n > 1:
        sort(0, n - 1)
    draw(arr)
    plt.show()
    return arr