def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key: # shiftselements that are greater than key value
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

#test
if __name__ == "__main__":
    #data = [13, 12, 11, 5, 6]
    data = [4, -2, -2, 8, 3, 1]
    print("Unsorted Data:", data)
    sorted_data = insertion_sort(data)
    print("Sorted Data:", sorted_data)