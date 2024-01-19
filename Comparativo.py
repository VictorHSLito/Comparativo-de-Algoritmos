import time
import random
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def test_bubble_sort(vector_size):
    arr = [random.randint(1, 1000) for _ in range(vector_size)]
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    return end_time - start_time


def test_quick_sort(vector_size):
    arr = [random.randint(1, 1000) for _ in range(vector_size)]
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    return end_time - start_time


def main():
    sizes = list(range(10, 10000, 20))
    times_bubble_sort = []
    times_quick_sort = []

    for size in sizes:
        elapsed_time_bubble_sort = test_bubble_sort(size)
        times_bubble_sort.append(elapsed_time_bubble_sort)

        elapsed_time_quick_sort = test_quick_sort(size)
        times_quick_sort.append(elapsed_time_quick_sort)

    plt.plot(sizes, times_bubble_sort, marker='o', linestyle='-', color='b', label='Bubble Sort', linewidth=1, markersize=2)
    plt.plot(sizes, times_quick_sort, marker='o', linestyle='-', color='r', label='Quick Sort', linewidth=1, markersize=2)

    plt.title('Bubble Sort vs Quick Sort')
    plt.xlabel('Tamanho do Vetor (n)')
    plt.ylabel('Tempo (s)')
    plt.grid(True)
    plt.legend()
    plt.show()


main()
