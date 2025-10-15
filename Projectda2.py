import time
import random
import math
import matplotlib.pyplot as plt
import numpy as np

# Insertion sort for small subgroups #

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Median-of-Medians QuickSelect Algorithm #

def median_of_medians(A, k):
    if len(A) <= 5:
        A = insertion_sort(A)
        return A[k]

    # Divide into groups of 5 and get medians #
    groups = [A[i:i + 5] for i in range(0, len(A), 5)]
    medians = [insertion_sort(group)[len(group)//2] for group in groups]

    # Find median of medians recursively #
    pivot = median_of_medians(medians, len(medians)//2)

    # Partition array around pivot #
    lows = [x for x in A if x < pivot]
    highs = [x for x in A if x > pivot]
    pivots = [x for x in A if x == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivot
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

# Experimental analysis #

n_values = [15, 16, 17, 18, 19, 20, 50, 100, 500, 1000, 2000, 4000, 8000, 16000, 32000]
exp_times = []
theo_values = []

for n in n_values:
    arr = [random.randint(1, 10000) for _ in range(n)]

    if n % 2 == 0:
        k1 = n // 2 - 1
        k2 = n // 2
        median_type = "Even"
    else:
        k1 = n // 2
        k2 = None
        median_type = "Odd"


    print(f"Input size (n): {n} ({median_type} elements)")
    print(f"Original array:\n{arr}")

    start = time.perf_counter()

    if k2 is None:
        median_val = median_of_medians(arr, k1)
    else:
        m1 = median_of_medians(arr, k1)
        m2 = median_of_medians(arr, k2)
        median_val = (m1 + m2) / 2

    end = time.perf_counter()

    sorted_arr = sorted(arr)
    print(f"\nSorted array:\n{sorted_arr}")

    if k2 is None:
        print(f"Median element (index={k1}): {median_val}")
    else:
        print(f"Median elements (indices={k1},{k2}): ({m1}, {m2}), Average = {median_val}")

    runtime_ms = (end - start) * 1e3
    print(f"Runtime: {runtime_ms:.6f} ms")

    exp_times.append(runtime_ms)
    theo_values.append(n)  # O(n) #

# Scaling and summary table #

avg_exp = np.mean(exp_times)
avg_theo = np.mean(theo_values)
scaling_factor = avg_exp / avg_theo
theo_scaled = [val * scaling_factor for val in theo_values]

print("Summary of Averages and Scaling")
print(f"Average Experimental Time (ms): {avg_exp:.6f}")
print(f"Average Theoretical Value     : {avg_theo:.6f}")
print(f"Scaling Factor (avg_exp/avg_theo): {scaling_factor:.6f}")

print("\nDetailed Table (Time in ms)")
print("n\tExperimental(ms)\tTheoretical\tScaled Theoretical(ms)")
for n, e, t, ts in zip(n_values, exp_times, theo_values, theo_scaled):
    print(f"{n}\t{e:.6f}\t\t{t:.6f}\t\t{ts:.6f}")

# Graph: Experimental vs Theoretical #

plt.figure(figsize=(10,6))
plt.plot(n_values, exp_times, marker='o', label="Experimental Runtime (ms)")
plt.plot(n_values, theo_scaled, marker='s', label="Theoretical (scaled, ms)")
plt.xlabel("Input size (n)")
plt.ylabel("Runtime (milliseconds)")
plt.title("QuickSelect – Median of Medians (O(n) Complexity)")
plt.legend()
plt.grid(True)
plt.show()
