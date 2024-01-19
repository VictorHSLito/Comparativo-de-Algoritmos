import time
import random
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def test_bubble_sort(vector_size):
    arr = [random.randint(1, 1000) for _ in range(vector_size)]
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    return end_time - start_time


def main():
    sizes = list(range(10, 10000, 20))
    times = []

    for size in sizes:
        elapsed_time = test_bubble_sort(size)
        times.append(elapsed_time)

    plt.plot(sizes, times, marker='o', linestyle='-', color='b', linewidth=1, markersize=2)
    plt.title('Algorito Bubble Sort')
    plt.xlabel('Tamanho do Vetor (n)')
    plt.ylabel('Tempo (s)')
    plt.grid(True)
    plt.show()


main()
