import timeit
import random

def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data[:])
    execution_time = timeit.default_timer() - start_time
    return sorted_data, execution_time

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Генеруємо випадкові дані для тестування
data_smallest = [random.randint(0, 1_000) for _ in range(10)]
data_small = [random.randint(0, 1_000) for _ in range(100)]
data_big = [random.randint(0, 1_000) for _ in range(1_000)]
data_largest = [random.randint(0, 10_000) for _ in range(10_000)]

test_data = [
    data_smallest,
    data_small,
    data_big,
    data_largest
]

sorting_functions = [
    insertion_sort,
    merge_sort,
    sorted,  # Timsort
]

# Порівняння алгоритмів сортування
results = {}
for sort_func in sorting_functions:
    func_name = sort_func.__name__
    results[func_name] = []
    for data in test_data:
        _, exec_time = measure_time(sort_func, data)
        results[func_name].append(exec_time)

# Виведення результатів
for func_name, times in results.items():
    print(f"{func_name}:")
    for i, time in enumerate(times):
        data_size = len(test_data[i])
        print(f"  Size {data_size}: {time:.6f} seconds")

# Додаткове порівняння з bubble_sort
_, bubble_sort_time = measure_time(bubble_sort, data_largest)
print(f"bubble_sort (size {len(data_largest)}): {bubble_sort_time:.6f} seconds")
