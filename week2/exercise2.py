from random import randint


def main():
    sample_values = [randint(0, 99) for _ in range(100)]  # Create 100 random integers.
    print("Original values:", sample_values)
    selection_sort(sample_values)
    print("Sorted values:  ", sample_values)


def swap(values, i, j):
    temp = values[i]
    values[i] = values[j]
    values[j] = temp


def selection_sort(values):
    for index_of_first_unsorted in range(len(values)):
        index_of_min = index_of_first_unsorted
        for i in range(index_of_first_unsorted + 1, len(values)):
            if values[i] < values[index_of_min]:
                index_of_min = i
        if index_of_min != index_of_first_unsorted:
            swap(values, index_of_first_unsorted, index_of_min)


if __name__ == "__main__":
    main()

"""
Counting constant-time operations in selection sort:
Line 18: n iterations
Line 19: 1 each time, n total
Line 20: n - 1 iterations the first time, then n - 2, n - 3, down to 0 iterations the last time, for a total of n * (n - 1) / 2 iterations
Line 21: 1 each time, n * (n - 1) / 2
Line 22: 0 or 1 each time, but since line 21 always runs, we can still say that these two lines in total perform n * (n - 1) / 2 constant-time operations
         (recall that a constant-time operation may still use a variable amount of time, as long as there is an input-independent limit on the time)
Line 23: 1 each time, n total
Line 24: 0 or 1 each time, n total (same argument as for line 21 and 22)

Summing all of this together and resolving all the parentheses, we will see that the highest-order term is n^2, so the complexity of selection sort is Θ(n^2).
Note that unlike insertion sort, selection sort does not have a best case that is better than the worst case; it performs the same number of iterations every time.
"""
