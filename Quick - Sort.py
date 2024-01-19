import random
import time
import matplotlib.pyplot as plt


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def test_quick_sort(array_size):
    data = [random.randint(0, 1000) for _ in range(array_size)]

    start_time = time.time()
    sorted_data = quick_sort(data)
    end_time = time.time()

    execution_time = end_time - start_time
    return execution_time


def main():
    sizes = list(range(10, 10000, 20))
    times = []

    for size in sizes:
        elapsed_time = test_quick_sort(size)
        times.append(elapsed_time)

    plt.plot(sizes, times, marker='o', linestyle='-', color='b', linewidth=1, markersize=2)
    plt.title('Algorito Quick Sort')
    plt.xlabel('Tamanho do Vetor (n)')
    plt.ylabel('Tempo (s)')
    plt.grid(True)
    plt.show()


main()
