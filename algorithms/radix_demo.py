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

SPEED = 0.03  # pause between frames (seconds)

def draw(arr, highlight=()):
    plt.cla()
    bars = plt.bar(range(len(arr)), arr)
    for i in highlight:
        if 0 <= i < len(arr):
            bars[i].set_color('r')
    plt.title("Radix Sort (LSD)")
    plt.pause(SPEED)

def radix_sort_lsd_nonneg_viz(arr, base=10):
    plt.figure()
    draw(arr)
    if not arr:
        plt.show()
        return arr
    if any(x < 0 for x in arr):
        plt.show()
        return arr  # nonneg version, skip if has negatives

    max_val = max(arr)
    exp = 1
    n = len(arr)
    out = [0] * n

    while max_val // exp > 0:
        count = [0] * base
        for x in arr:
            digit = (x // exp) % base
            count[digit] += 1
        for i in range(1, base):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            digit = (arr[i] // exp) % base
            count[digit] -= 1
            pos = count[digit]
            out[pos] = arr[i]
            draw(out, (pos,))  # show placement in this digit pass
        arr[:] = out
        draw(arr)             # show after finishing this digit
        exp *= base

    draw(arr)
    plt.show()
    return arr

def radix_sort_lsd_viz(arr, base=10):
    # handles negatives by splitting
    plt.figure()
    draw(arr)
    neg = [-x for x in arr if x < 0]
    pos = [x for x in arr if x >= 0]

    # visualize pos part
    if pos:
        max_val = max(pos)
        exp = 1
        out = [0] * len(pos)
        while max_val // exp > 0:
            count = [0] * base
            for x in pos:
                count[(x // exp) % base] += 1
            for i in range(1, base):
                count[i] += count[i - 1]
            for i in range(len(pos) - 1, -1, -1):
                d = (pos[i] // exp) % base
                count[d] -= 1
                out[count[d]] = pos[i]
                # draw combined snapshot (neg reversed later)
                snapshot = [-v for v in sorted(neg, reverse=True)] + out + [0] * (len(pos) - 1 - i)
                draw(snapshot)
            pos[:] = out
            draw(neg[::-1] + pos)
            exp *= base

    # visualize neg part (sort abs and then reverse)
    if neg:
        max_val = max(neg)
        exp = 1
        out = [0] * len(neg)
        while max_val // exp > 0:
            count = [0] * base
            for x in neg:
                count[(x // exp) % base] += 1
            for i in range(1, base):
                count[i] += count[i - 1]
            for i in range(len(neg) - 1, -1, -1):
                d = (neg[i] // exp) % base
                count[d] -= 1
                out[count[d]] = neg[i]
                snapshot = [-v for v in out] + pos
                draw(snapshot)
            neg[:] = out
            draw([-v for v in neg] + pos)
            exp *= base

    neg_sorted = [-v for v in neg][::-1]  # more negative first
    arr[:] = neg_sorted + pos
    draw(arr)
    plt.show()
    return arr