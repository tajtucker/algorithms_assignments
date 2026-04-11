import time
import random
from counting_sort import counting_sort
from quick_sort import quick_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from heap_sort import heap_sort
from selection_sort import selection_sort

def generate_dataset(size):
    return [random.randint(1, 999998) for _ in range(size)]

def dataset_time(algo, data):
    times=[]
    for i in range(3):
        start = time.perf_counter()
        algo(data.copy())
        end = time.perf_counter()
        times.append(end-start)
        print(f"Run {i+1} for {algo.__name__}: {end - start:.6f} seconds")
    avg = sum(times) / len(times)
    return f"Average time of {algo.__name__}: {avg:.6f} seconds"

algorithms = [
    merge_sort,
    quick_sort,
    heap_sort,
    counting_sort,
    insertion_sort,
    selection_sort
]
sizes = [10000, 50000, 100000, 500000, 1000000]
for size in sizes:
    data = generate_dataset(size)
    print(f"\nDataset Size: {size}")
    for algo in algorithms:
        print(dataset_time(algo, data))