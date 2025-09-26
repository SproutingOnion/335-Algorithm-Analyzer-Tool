# radix sort (lsd) that will support non negative integers directly.
# providing wrapper to handle negatives as well
# Demo of real world scenario - sorting order records by order_id

from typing import List, Dict, Tuple
import time
import random
import matplotlib.pyplot as plt


# Core: stable counting sort by one digit (base would be 10 by default)

def _counting_sort_by_digits(a: List[int], exp: int, base: int = 10) -> None:
    n = len(a)
    output = [0] * n
    count = [0] * base

    # 1 Count occurances of this digit among all #s
    for i in range(n):
        digit = (a[i] // exp) % base
        count[digit] += 1

    # 2 Prefix Sums: transform counts into ending positiosn
    for d in range(1, base):
        count[d] += count[d - 1]

    # 3 Stable write: traverse input backwards to preserve the order of equal digits
    for i in range(n - 1, -1, -1):
        digit = (a[i] // exp) % base
        pos = count[digit] - 1
        output[pos] = a[i]
        count[digit] -= 1

    # 4 Copy Back: traverse input backwards to preserve the order of equal digits
    for i in range(n):
        a[i] = output[i]


# Define Radix Sort LSD for Non Negative Integers
def radix_sort_lsd_nonneg(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a

    start = time.perf_counter()  # Starting high resolution timer for benchmarking (in seconds)

    max_val = max(a)
    exp = 1

    while max_val // exp > 0:
        _counting_sort_by_digits(a, exp, base)
        exp *= base

    end = time.perf_counter()
    print(f"[Radix] nonneg sort in {end - start:.6f} sec (base={base})")
    return a


# Handling negative value
def radix_sort_lsd(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a

    neg = [-x for x in a if x < 0]
    pos = [x for x in a if x >= 0]

    # Sort both subsets
    if neg:
        radix_sort_lsd_nonneg(neg, base)
    if pos:
        radix_sort_lsd_nonneg(pos, base)

    neg_sorted = [-x for x in reversed(neg)]

    out = neg_sorted + pos
    return out


# Real world scenario - Sorting Order Records
def sort_orders_by_id(orders: List[Dict], key: str = "order_id", base: int = 10) -> List[Dict]:
    if not orders:
        return orders

    keys = []
    index = []

    for i, rec in enumerate(orders):
        keys.append(int(rec[key]))
        index.append(i)

    def stable_pass_with_companion(keys: List[int], comp: List[int], exp: int, base: int) -> None:
        n = len(keys)
        out_keys = [0] * n
        out_comp = [0] * n
        count = [0] * base
        for i in range(n):
            d = (keys[i] // exp) % base
            count[d] += 1
        for d in range(1, base):
            count[d] += count[d - 1]
        for i in range(n - 1, -1, -1):
            d = (keys[i] // exp) % base
            pos = count[d] - 1
            out_keys[pos] = keys[i]
            out_comp[pos] = comp[i]
            count[d] -= 1
        for i in range(n):
            keys[i] = out_keys[i]
            comp[i] = out_comp[i]

    # Run LSD Passes
    max_key = max(keys)
    exp = 1
    start = time.perf_counter()
    while max_key // exp > 0:
        stable_pass_with_companion(keys, index, exp, base)
        exp *= base
    end = time.perf_counter()
    print(f"[Radix] Order sort in {end - start:.6f} sec for {len(orders)} records")

    sorted_orders = [orders[i] for i in index]
    return sorted_orders

SPEED = 0.03
PAUSE = {'v': True}
FIG = {'obj': None}

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Radix Sort (LSD)")
    plt.pause(SPEED)
    # pause loop (Space toggles)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def radix_sort_lsd_viz(arr, base=10):
    plt.figure()
    fig = plt.gcf()

    FIG['obj'] = fig
    fig.canvas.mpl_connect('close_event', lambda e: FIG.update(obj=None))

    def on_key(e):
        k = (e.key or '')
        if k == ' ' or k.lower() == 'space':
            PAUSE['v'] = not PAUSE['v']     # play/pause
        elif k.lower() in ('r', 'q', 'escape', 'esc'):
            plt.close(FIG['obj'] if FIG['obj'] is not None else fig)  # reset/quit

    fig.canvas.mpl_connect('key_press_event', on_key)
    ...


    PAUSE['v'] = True
    try:
        plt.gcf().canvas.manager.set_window_title(
            "Radix (LSD, non-negative) — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True                       # start paused
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    if not arr or any(x < 0 for x in arr):
        plt.show()
        return arr

    n = len(arr)
    out = [0] * n
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        count = [0] * base
        for x in arr:
            count[(x // exp) % base] += 1

        for i in range(1, base):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            d = (arr[i] // exp) % base
            count[d] -= 1
            pos = count[d]
            out[pos] = arr[i]
            draw(out, (pos,))              # show placement
            if not plt.fignum_exists(fig.number):
                return arr

        arr[:] = out
        draw(arr)                           # after finishing this digit
        if not plt.fignum_exists(fig.number):
            return arr
        exp *= base

    draw(arr)                                # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr

def radix_sort_lsd_viz(arr, base=10):
    plt.figure()
    fig = plt.gcf()

    def on_key(e):
        if e.key == ' ':
            PAUSE['v'] = not PAUSE['v']     # play/pause
        elif e.key in ('r', 'escape', 'q'):
            plt.close(fig)                  # reset/quit

    fig.canvas.mpl_connect('key_press_event', on_key)
    try:
        plt.gcf().canvas.manager.set_window_title(
            "Radix (LSD, signed) — Space=Play/Pause, R=Reset, Q/Esc=Quit"
        )
    except Exception:
        pass

    PAUSE['v'] = True
    draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr

    # split into negatives (by absolute) and non-negatives
    neg = [-x for x in arr if x < 0]   # store absolute values
    pos = [x for x in arr if x >= 0]

    # helper: in-place LSD on a list of non-negative ints, visualizing combined snapshot
    def lsd_inplace(a, title_after_pass=None):
        if not a:
            return
        out = [0] * len(a)
        m = max(a)
        exp = 1
        while m // exp > 0:
            count = [0] * base
            for x in a:
                count[(x // exp) % base] += 1
            for i in range(1, base):
                count[i] += count[i - 1]
            for i in range(len(a) - 1, -1, -1):
                d = (a[i] // exp) % base
                count[d] -= 1
                out[count[d]] = a[i]
                # draw current combined snapshot: (-neg_sorted desc) + pos_partial
                combined = [-v for v in sorted(neg, reverse=True)] + out + [0] * (len(a) - 1 - i)
                draw(combined)
                if not plt.fignum_exists(fig.number):
                    return
            a[:] = out
            draw([-v for v in sorted(neg, reverse=True)] + a)  # after this digit
            if not plt.fignum_exists(fig.number):
                return
            exp *= base

    # sort positives by LSD
    lsd_inplace(pos)

    # sort abs(negatives) by LSD, then convert back to negatives and reverse (more negative first)
    def lsd_inplace_simple(a):
        if not a:
            return
        out = [0] * len(a)
        m = max(a)
        exp = 1
        while m // exp > 0:
            count = [0] * base
            for x in a:
                count[(x // exp) % base] += 1
            for i in range(1, base):
                count[i] += count[i - 1]
            for i in range(len(a) - 1, -1, -1):
                d = (a[i] // exp) % base
                count[d] -= 1
                out[count[d]] = a[i]
                combined = [-v for v in out] + pos
                draw(combined)
                if not plt.fignum_exists(fig.number):
                    return
            a[:] = out
            draw([-v for v in a] + pos)
            if not plt.fignum_exists(fig.number):
                return
            exp *= base

    lsd_inplace_simple(neg)

    neg_sorted = [-v for v in neg][::-1]
    arr[:] = neg_sorted + pos
    draw(arr)                                 # final frame
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr