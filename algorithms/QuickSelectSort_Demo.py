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

SPEED = 0.03
PAUSE = {'v': True}
FIG = {'obj': None}

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Quick Select")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def quick_select_viz(arr, k):
    # k is 0-based index
    if not arr or k < 0 or k >= len(arr):
        return None

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
            "Quick Select — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                        # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return None

    low, high = 0, len(arr) - 1
    while low <= high and plt.fignum_exists(fig.number):
        pivot = arr[high]                     # Lomuto partition (pivot at high)
        i = low
        draw(arr, (high,))                    # show pivot
        if not plt.fignum_exists(fig.number):
            return None

        for j in range(low, high):
            draw(arr, (j, high))              # compare with pivot
            if not plt.fignum_exists(fig.number):
                return None
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                draw(arr, (i, j))             # show swap
                if not plt.fignum_exists(fig.number):
                    return None
                i += 1

        arr[i], arr[high] = arr[high], arr[i]
        draw(arr, (i,))                       # pivot placed
        if not plt.fignum_exists(fig.number):
            return None

        if k == i:
            draw(arr, (i,))
            if plt.fignum_exists(fig.number):
                plt.show()
            return arr[i]
        elif k < i:
            high = i - 1
        else:
            low = i + 1

    if plt.fignum_exists(fig.number):
        plt.show()
    return None
