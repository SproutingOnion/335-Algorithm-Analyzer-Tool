# Main file for UI interface and calling sorting algorithms
VISUALIZE = True
from typing import Callable, List, Dict, Tuple
import random
import pygame
import time
from algorithms.radix_demo import *
from algorithms.HeapSort_demo import *
from algorithms.mergesort_demo import *
from algorithms.QuickSelectSort_Demo import *
from algorithms.QuickSort_demo import *
from algorithms.bubblesort_demo import *
from algorithms.BucketSort_Demo import *
from algorithms.countingsort_demo import *
from algorithms.insertsort_demo import *

# --------- Config ---------
SCREEN_W, SCREEN_H = 800, 600
BG = (18, 18, 22)
FG = (230, 230, 235)
ACCENT = (120, 180, 255)
MUTED = (150, 150, 160)

MENU_TITLE = "Sorting Demo"
FONT_NAME = None  # default system font
LIST_SIZE_RANGE = (10, 50)  # random size each run
INT_RANGE = (1, 200)
FLOAT_DECIMALS_TO_PRINT = 3  # only for preview printed to console


# --------- Data Generators ---------
def make_int_list() -> List[int]:
    n = random.randint(*LIST_SIZE_RANGE)
    return [random.randint(*INT_RANGE) for _ in range(n)]


def make_float_list() -> List[float]:
    n = random.randint(*LIST_SIZE_RANGE)
    return [random.random() for _ in range(n)]


# --------- Wrappers to standardize timing & output ---------
def run_and_time(func: Callable[..., any], *args, **kwargs) -> Tuple[any, float]:
    start = time.perf_counter()
    result = func(*args, **kwargs)
    elapsed = time.perf_counter() - start
    return result, elapsed


def run_merge_sort() -> Tuple[str, float]:
    data = make_int_list()
    if VISUALIZE:
        from algorithms.mergesort_demo import merge_sort_viz
        merge_sort_viz(data.copy())
    sorted_list, t = run_and_time(merge_sort, data)
    print("\n[Merge Sort] input:", data)
    print("[Merge Sort] output:", sorted_list)
    print(f"[Merge Sort] time: {t:.6f} sec")
    return "Merge Sort", t


def run_radix_sort() -> Tuple[str, float]:
    data = make_int_list()
    base = 10
    if VISUALIZE:
        from algorithms.radix_demo import radix_sort_lsd_nonneg_viz
        radix_sort_lsd_nonneg_viz(data.copy())
    sorted_list, t = run_and_time(radix_sort_lsd_nonneg, data, base)
    print("\n[Radix LSD] input:", data)
    print("[Radix LSD] output:", sorted_list)
    print(f"[Radix LSD] base={base} time: {t:.6f} sec")
    return "Radix Sort (LSD)", t


def run_bubble_sort() -> Tuple[str, float]:
    data = make_int_list()
    if VISUALIZE:
        from algorithms.bubblesort_demo import bubble_sort_viz
        bubble_sort_viz(data.copy())
    sorted_list, t = run_and_time(bubble_sort, data)
    print("\n[Bubble Sort] input:", data)
    print("[Bubble Sort] output:", sorted_list)
    print(f"[Bubble Sort] time: {t:.6f} sec")
    return "Bubble Sort", t


def run_bucket_sort() -> Tuple[str, float]:
    data = make_float_list()
    if VISUALIZE:
        from algorithms.BucketSort_Demo import bucket_sort_viz
        bucket_sort_viz(data.copy())

    sorted_list, t = run_and_time(bucket_sort, data)
    # print floats briefly
    preview_in = [round(x, FLOAT_DECIMALS_TO_PRINT) for x in data]
    preview_out = [round(x, FLOAT_DECIMALS_TO_PRINT) for x in sorted_list]
    print("\n[Bucket Sort] input:", preview_in)
    print("[Bucket Sort] output:", preview_out)
    print(f"[Bucket Sort] time: {t:.6f} sec")
    return "Bucket Sort (floats)", t


def run_counting_sort() -> Tuple[str, float]:
    data = make_int_list()
    if VISUALIZE:
        from algorithms.countingsort_demo import counting_sort_viz
        counting_sort_viz(data.copy())
    sorted_list, t = run_and_time(counting_sort, data)
    print("\n[Counting Sort] input:", data)
    print("[Counting Sort] output:", sorted_list)
    print(f"[Counting Sort] time: {t:.6f} sec")
    return "Counting Sort", t


def run_insertion_sort() -> Tuple[str, float]:
    data = make_int_list()
    if VISUALIZE:
        from algorithms.insertsort_demo import insertion_sort_viz
        insertion_sort_viz(data.copy())
    sorted_list, t = run_and_time(insertion_sort, data)
    print("\n[Insertion Sort] input:", data)
    print("[Insertion Sort] output:", sorted_list)
    print(f"[Insertion Sort] time: {t:.6f} sec")
    return "Insertion Sort", t


def run_heap_sort() -> Tuple[str, float]:
    data = make_int_list()
    if VISUALIZE:
        from algorithms.HeapSort_demo import heap_sort_viz
        heap_sort_viz(data.copy())
    sorted_list, t = run_and_time(heap_sort, data)
    print("\n[Heap Sort] input:", data)
    print("[Heap Sort] output:", sorted_list)
    print(f"[Heap Sort] time: {t:.6f} sec")
    return "Heap Sort", t


def run_quick_sort() -> Tuple[str, float]:
    data = make_int_list()
    if VISUALIZE:
        from algorithms.QuickSort_demo import quick_sort_viz
        quick_sort_viz(data.copy())
    sorted_list, t = run_and_time(quick_sort, data)
    print("\n[Quick Sort] input:", data)
    print("[Quick Sort] output:", sorted_list)
    print(f"[Quick Sort] time: {t:.6f} sec")
    return "Quick Sort", t


def run_quick_select_median() -> Tuple[str, float]:
    data = make_int_list()
    k = len(data) // 2
    if VISUALIZE:
        from algorithms.QuickSelectSort_Demo import quick_select_viz
        quick_select_viz(data.copy(), k)
    value, t = run_and_time(quick_select, data, 0, len(data) - 1, k)
    print("\n[Quick Select] median k =", k, "input:", data)
    print("[Quick Select] value:", value)
    print(f"[Quick Select] time: {t:.6f} sec")
    return "Quick Select (median)", t



MENU_ITEMS = [
    ("Merge Sort", run_merge_sort, ""),
    ("Radix Sort (LSD, base 10)", run_radix_sort, ""),
    ("Bubble Sort", run_bubble_sort, ""),
    ("Bucket Sort (floats)", run_bucket_sort, "Generates random floats"),
    ("Counting Sort", run_counting_sort, f"Range {INT_RANGE[0]}-{INT_RANGE[1]}"),
    ("Insertion Sort", run_insertion_sort, ""),
    ("Heap Sort", run_heap_sort, ""),
    ("Quick Sort", run_quick_sort, ""),
    ("Quick Select (median)", run_quick_select_median, "Not a full sort"),
]


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption(MENU_TITLE)
    clock = pygame.time.Clock()

    title_font = pygame.font.Font(FONT_NAME, 40)
    item_font = pygame.font.Font(FONT_NAME, 28)
    small_font = pygame.font.Font(FONT_NAME, 20)

    selected = 0
    last_run_label = "—"
    last_run_time = None
    running = True

    def render_text(text, font, color):
        return font.render(text, True, color)

    while running:
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    selected = (selected - 1) % len(MENU_ITEMS)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    selected = (selected + 1) % len(MENU_ITEMS)
                elif event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    # run selected
                    label, runner, _ = MENU_ITEMS[selected]
                    try:
                        last_run_label, last_run_time = runner()
                    except Exception as e:
                        print(f"[ERROR] while running {label}: {e}")
                        last_run_label, last_run_time = f"{label} (error)", None
                elif event.key == pygame.K_ESCAPE:
                    running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        screen.fill(BG)

        # Title
        title_surf = render_text(MENU_TITLE, title_font, FG)
        screen.blit(title_surf, (40, 30))

        # Hint line
        hint = "Esc to quit"
        hint_surf = render_text(hint, small_font, MUTED)
        screen.blit(hint_surf, (40, 80))

        # Draw menu items
        start_y = 130
        line_h = 48
        hovered_index = None

        for i, (label, _, subtitle) in enumerate(MENU_ITEMS):
            y = start_y + i * line_h
            # Hitbox for mouse selection
            rect = pygame.Rect(40, y - 6, SCREEN_W - 80, line_h)
            is_hovered = rect.collidepoint(mouse_pos)
            if is_hovered:
                hovered_index = i

            # Visual state
            color = ACCENT if (i == selected or is_hovered) else FG
            label_surf = render_text(label, item_font, color)
            screen.blit(label_surf, (60, y))

            if subtitle:
                sub_surf = render_text(subtitle, small_font, MUTED)
                screen.blit(sub_surf, (60, y + 24))

            # Mouse click = run
            if is_hovered and mouse_clicked:
                selected = i
                try:
                    run_label, run_time = MENU_ITEMS[i][1]()
                    last_run_label, last_run_time = run_label, run_time
                except Exception as e:
                    print(f"[ERROR] while running {label}: {e}")
                    last_run_label, last_run_time = f"{label} (error)", None

        # Bottom panel with last run info
        pygame.draw.rect(screen, (28, 28, 34), (0, SCREEN_H - 110, SCREEN_W, 110))
        footer_title = "Last Run:"
        footer_title_surf = render_text(footer_title, item_font, FG)
        screen.blit(footer_title_surf, (40, SCREEN_H - 100))

        if last_run_time is None and last_run_label == "—":
            msg = "No algorithm run yet."
        elif last_run_time is None:
            msg = f"{last_run_label} — error (see console)"
        else:
            msg = f"{last_run_label} finished in {last_run_time:.6f} sec"
        footer_msg_surf = render_text(msg, small_font, FG)
        screen.blit(footer_msg_surf, (40, SCREEN_H - 64))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

# #Demo to test out for calling functions from files and using random int generators
# #To test with other algorithsm comment out other __name__ == __main__  from respective files
# if __name__ == "__main__":
#    random_index_size = random.randint(1,50) #Sets index ranging from 1 - 50

#    #Filling the list with numbers from 1 - 200. May be increased if need to
#    random_filled_list = [random.randint(1, 200) for i in range(random_index_size)] #Random int filled list
#    random_filled_float_list = [random.random() for i in range(random_index_size)] #Random float filled list

#    base = 10 #Printing purposes but it shows base number for radix sort. May be user inputted if necessary

#    #Mergre sort time counter in main due to recursion in algorithm
#    start = time.perf_counter()
#    sorted = merge_sort(random_filled_list)
#    end = time.perf_counter()
#    print(f"[Mergre] sort in {end-start:.6f} sec")
#    print(sorted)


#    print(radix_sort_lsd_nonneg(random_filled_list,10))

#    print(bubble_sort(random_filled_list))

#    print(bucket_sort(random_filled_float_list)) #Proabably shorten float to 2 significant digits (dont know how)

#    print(counting_sort(random_filled_list))

#    print(insertion_sort(random_filled_list))

#    print(heap_sort(random_filled_list))

#    print(quick_sort(random_filled_list))

#    timed_quick_select(random_filled_list,  len(random_filled_list) // 2)
