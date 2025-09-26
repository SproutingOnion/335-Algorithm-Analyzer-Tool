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

SPEED = 0.05
PAUSE = {'v': True}
FIG = {'obj': None}

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Merge Sort")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def merge_sort_viz(arr):
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
            "Merge Sort — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                        # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    n = len(arr)
    temp = [0] * n

    # read from temp, write into arr (prevents overwriting unread values)
    def merge(lo, mid, hi):
        temp[lo:hi+1] = arr[lo:hi+1]
        i, j, k = lo, mid + 1, lo
        while i <= mid and j <= hi:
            if temp[i] <= temp[j]:
                arr[k] = temp[i]
                draw(arr, (k,))
                if not plt.fignum_exists(fig.number):
                    return
                i += 1
            else:
                arr[k] = temp[j]
                draw(arr, (k,))
                if not plt.fignum_exists(fig.number):
                    return
                j += 1
            k += 1
        while i <= mid:
            arr[k] = temp[i]
            draw(arr, (k,))
            if not plt.fignum_exists(fig.number):
                return
            i += 1
            k += 1
        while j <= hi:
            arr[k] = temp[j]
            draw(arr, (k,))
            if not plt.fignum_exists(fig.number):
                return
            j += 1
            k += 1

    def sort(lo, hi):
        if lo >= hi:
            return
        mid = (lo + hi) // 2
        sort(lo, mid)
        if not plt.fignum_exists(fig.number):
            return
        sort(mid + 1, hi)
        if not plt.fignum_exists(fig.number):
            return
        merge(lo, mid, hi)

    if n > 1:
        sort(0, n - 1)

    draw(arr)                                  # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr