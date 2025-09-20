import time
from typing import List, Any

def binary_search(arr: List[Any], target: Any) -> int:

    left, right = 0, len(arr) -1

    while left <= right:
        mid = (left + right) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def timed_binary_search(arr: List[Any], target: Any) -> int:

    start = time.perf_counter()
    result = binary_search(arr, target)
    end = time.perf_counter()
    print(f"[Binary] Search n = {len(arr)} in {end-start:.6f} seconds; result index = {result}")
    return result

#Example Application
product_ids = [101, 150, 204, 207, 765, 876]
print("Search 765:", timed_binary_search(product_ids, 765))
print("Search 201:", timed_binary_search(product_ids, 201))