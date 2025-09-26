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

SPEED = 0.05
PAUSE = {'v': True}
FIG = {'obj': None}

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Bucket Sort")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def bucket_sort_viz(arr):
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
            "Bucket Sort — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                        # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    n = len(arr)
    if n == 0:
        plt.show()
        return arr

    # create buckets and distribute values (assuming values in [0, 1))
    buckets = [[] for _ in range(n)]
    for x in arr:
        idx = int(n * x)
        if idx >= n:                         # guard if x == 1.0
            idx = n - 1
        buckets[idx].append(x)

    # sort each bucket (in-place)
    for b in buckets:
        b.sort()

    # concatenate back with visualization
    k = 0
    for b in buckets:
        for v in b:
            arr[k] = v
            draw(arr, (k,))                  # show placement
            if not plt.fignum_exists(fig.number):
                return arr
            k += 1

    draw(arr)                                 # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr

