def counting_sort(arr):
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

    return output

if __name__ == "__main__":
    data = [4, -2, -2, 8, 3, 1]
    print("Unsorted Data:", data)
    sorted_data = counting_sort(data)
    print("Sorted Data:", sorted_data)