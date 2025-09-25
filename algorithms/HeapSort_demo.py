import time
import matplotlib.pyplot as plt

def heap_sort(arr):
# heap sort would be in place as wrst case efficiency with
    start = time.perf_counter()
    def sift_down(a, start, end):
        root = start
        while (left := 2 * root + 1) <= end:
            right = left + 1
            largest = root
            if a[left] > a[largest]:
                largest = left
            if right <= end and a[right] > a[largest]:
                largest = right
            if largest == root:
                break
            a[root], a[largest] = a[largest], a[root]
            root = largest
    def build_max_heap(a):
        n = len(a)
        for i in range (n // 2 - 1, -1, -1):
            sift_down(a, i, n - 1)
    a = arr
    n = len(a)
    build_max_heap(a)
    for end in range(n - 1, 0, -1):
        a[0], a[end] = a[end], a[0]
        sift_down(a, 0, end -1)
    end = time.perf_counter()
    print(f"[Heap] sort in {end - start:.6f} sec")
    return a

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Heap Sort")
    plt.pause(SPEED)

def heap_sort_viz(arr):
    plt.figure()
    draw(arr)
    n = len(arr)

    def sift_down_viz(a, start, end):
        root = start
        while (left := 2 * root + 1) <= end:
            right = left + 1
            largest = root
            # compare with left
            draw(a, (root, left))
            if a[left] > a[largest]:
                largest = left
            # compare with right
            if right <= end:
                draw(a, (largest, right))
                if a[right] > a[largest]:
                    largest = right
            if largest == root:
                break
            a[root], a[largest] = a[largest], a[root]
            draw(a, (root, largest))  # show swap
            root = largest

    # build max heap
    for start in range((n // 2) - 1, -1, -1):
        sift_down_viz(arr, start, n - 1)

    # sort down
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        draw(arr, (0, end))           # move max to the end
        sift_down_viz(arr, 0, end - 1)

    draw(arr)
    plt.show()
    return arr




