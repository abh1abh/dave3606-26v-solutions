import random
import time
from week2.exercise2 import selection_sort
from week2.exercise3 import merge_sort


def main():
    sample_array = create_large_array(1000)
    t = time.time()
    selection_sort(sample_array)
    t = time.time() - t
    print("Time taken for Selection Sort:", t, "seconds")

    t = time.time()
    merge_sort(sample_array)
    t = time.time() - t
    print("Time taken for Merge Sort:", t, "seconds")

    t = time.time()
    sample_array.sort()
    t = time.time() - t
    print("Time taken for Python's built-in sort:", t, "seconds")


def create_large_array(size):
    return [random.randint(0, 10000) for _ in range(size)]


if __name__ == "__main__":
    main()

# Python 3.11 uses Powersort for its built-in `sort` and `sorted` functions: https://en.wikipedia.org/wiki/Powersort.
