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

SPEED = 0.05
PAUSE = {'v': True}
FIG = {'obj': None}

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Counting Sort")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def counting_sort_viz(arr):
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
            "Counting Sort — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                        # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    if not arr:
        plt.show()
        return arr

    # standard counting sort (visualizing placements)
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
        draw(res, (pos,))                    # show each placement
        if not plt.fignum_exists(fig.number):
            return arr

    arr[:] = res                              # write back
    draw(arr)                                 # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr