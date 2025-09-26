# algorithms/radix_demo.py
from typing import List, Dict
import time
import matplotlib.pyplot as plt

def _counting_sort_by_digits(a: List[int], exp: int, base: int = 10) -> None:
    n = len(a)
    output = [0] * n
    count = [0] * base
    for i in range(n):
        digit = (a[i] // exp) % base
        count[digit] += 1
    for d in range(1, base):
        count[d] += count[d - 1]
    for i in range(n - 1, -1, -1):
        digit = (a[i] // exp) % base
        pos = count[digit] - 1
        output[pos] = a[i]
        count[digit] -= 1
    for i in range(n):
        a[i] = output[i]

def radix_sort_lsd_nonneg(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a
    start = time.perf_counter()
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        _counting_sort_by_digits(a, exp, base)
        exp *= base
    end = time.perf_counter()
    print(f"[Radix] nonneg sort in {end - start:.6f} sec (base={base})")
    return a

def radix_sort_lsd(a: List[int], base: int = 10) -> List[int]:
    if not a:
        return a
    neg = [-x for x in a if x < 0]
    pos = [x for x in a if x >= 0]
    if neg:
        radix_sort_lsd_nonneg(neg, base)
    if pos:
        radix_sort_lsd_nonneg(pos, base)
    neg_sorted = [-x for x in reversed(neg)]
    out = neg_sorted + pos
    return out

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

def _draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Radix Sort (LSD)")
    plt.pause(SPEED)
    while PAUSE['v'] and FIG['obj'] is not None and plt.fignum_exists(FIG['obj'].number):
        plt.pause(0.05)

def radix_sort_lsd_nonneg_viz(arr: List[int], base: int = 10):
    fig = plt.figure()
    FIG['obj'] = fig
    def on_key(e):
        k = (e.key or '')
        if k == ' ' or k.lower() == 'space':
            PAUSE['v'] = not PAUSE['v']
        elif k.lower() in ('r', 'q', 'escape', 'esc'):
            plt.close(FIG['obj'] if FIG['obj'] is not None else fig)
    fig.canvas.mpl_connect('close_event', lambda e: FIG.update(obj=None))
    fig.canvas.mpl_connect('key_press_event', on_key)
    try:
        plt.gcf().canvas.manager.set_window_title("Radix (LSD, non-negative) — Space=Play/Pause, R=Reset, Q/Esc=Quit")
    except Exception:
        pass
    PAUSE['v'] = True
    _draw(arr)
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
            snapshot = out.copy()
            zeros_to_fill = n - 1 - i
            for z in range(zeros_to_fill):
                snapshot[n - 1 - z] = snapshot[n - 1 - z] if snapshot[n - 1 - z] != 0 else 0
            _draw(snapshot, (pos,))
            if not plt.fignum_exists(fig.number):
                return arr
        arr[:] = out
        _draw(arr)
        if not plt.fignum_exists(fig.number):
            return arr
        exp *= base
    _draw(arr)
    if not plt.fignum_exists(fig.number):
        return arr
    plt.show()
    return arr
