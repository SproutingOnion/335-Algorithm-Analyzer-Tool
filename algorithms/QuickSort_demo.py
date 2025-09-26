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

SPEED = 0.05
PAUSE = {'v': True}
FIG = {'obj': None}

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Quick Sort")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def quick_sort_viz(arr):
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
            "Quick Sort — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                        # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    def partition_viz(low, high):
        pivot = arr[(low + high) // 2]
        i, j = low, high
        draw(arr, (i, j))                    # show current bounds
        if not plt.fignum_exists(fig.number):
            return i, j
        while i <= j:
            while arr[i] < pivot:
                i += 1
                draw(arr, (i, j))            # move i →
                if not plt.fignum_exists(fig.number):
                    return i, j
            while arr[j] > pivot:
                j -= 1
                draw(arr, (i, j))            # ← move j
                if not plt.fignum_exists(fig.number):
                    return i, j
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                draw(arr, (i, j))            # show swap
                if not plt.fignum_exists(fig.number):
                    return i, j
                i += 1
                j -= 1
        return i, j

    def sort_viz(low, high):
        if low < high:
            i, j = partition_viz(low, high)
            if not plt.fignum_exists(fig.number):
                return
            if low < j:
                sort_viz(low, j)
                if not plt.fignum_exists(fig.number):
                    return
            if i < high:
                sort_viz(i, high)

    sort_viz(0, len(arr) - 1)
    draw(arr)                                 # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr