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

SPEED = 0.05
PAUSE = {'v': True}
FIG = {'obj': None}

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Heap Sort")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def heap_sort_viz(arr):
    plt.figure()
    fig = plt.gcf()

    FIG['obj'] = fig
    fig.canvas.mpl_connect('close_event', lambda e: FIG.update(obj=None))

    def on_key(e):
        k = (e.key or '')
        if k == ' ' or k.lower() == 'space':
            PAUSE['v'] = not PAUSE['v']
        elif k.lower() in ('r', 'q', 'escape', 'esc'):
            plt.close(FIG['obj'] if FIG['obj'] is not None else fig)

    fig.canvas.mpl_connect('key_press_event', on_key)

    PAUSE['v'] = True
    try:
        plt.gcf().canvas.manager.set_window_title(
            "Heap Sort — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                      # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    n = len(arr)

    def sift_down_viz(a, start, end):
        root = start
        while (left := 2 * root + 1) <= end:
            right = left + 1
            largest = root

            # compare root with left
            draw(a, (root, left))
            if not plt.fignum_exists(fig.number):
                return
            if a[left] > a[largest]:
                largest = left

            # compare current largest with right
            if right <= end:
                draw(a, (largest, right))
                if not plt.fignum_exists(fig.number):
                    return
                if a[right] > a[largest]:
                    largest = right

            if largest == root:
                return
            a[root], a[largest] = a[largest], a[root]
            draw(a, (root, largest))       # show swap
            if not plt.fignum_exists(fig.number):
                return
            root = largest

    # build max-heap
    for start in range((n // 2) - 1, -1, -1):
        sift_down_viz(arr, start, n - 1)
        if not plt.fignum_exists(fig.number):
            return arr

    # sort down
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        draw(arr, (0, end))                # move max to end
        if not plt.fignum_exists(fig.number):
            return arr
        sift_down_viz(arr, 0, end - 1)
        if not plt.fignum_exists(fig.number):
            return arr

    draw(arr)                               # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr




