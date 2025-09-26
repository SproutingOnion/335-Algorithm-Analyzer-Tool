import time
import matplotlib.pyplot as plt

def insertion_sort(arr):
    start = time.perf_counter()
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key: # shiftselements that are greater than key value
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    end = time.perf_counter()
    print(f"[Insert] sort in {end-start:.6f} sec.")
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
    plt.title("Insertion Sort")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def insertion_sort_viz(arr):
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
            "Insertion Sort — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                      # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        draw(arr, (j, i))                  # initial comparison
        if not plt.fignum_exists(fig.number):
            return arr
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]            # shift
            j -= 1
            draw(arr, (j, j + 1))          # show shift positions
            if not plt.fignum_exists(fig.number):
                return arr
        arr[j + 1] = key                   # insert key
        draw(arr, (j + 1,))                # show insertion
        if not plt.fignum_exists(fig.number):
            return arr

    draw(arr)                               # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr