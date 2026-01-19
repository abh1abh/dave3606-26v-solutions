def main():
    list_a = [9, 4, 7, 1, 7, 3, 4]
    list_b = [2, 3, 1, 7, 3, 9, 8, 7, 6]
    # The list function creates a copy of an existing list.
    # We do this to show that the sorting that is done by
    # intersection_sort_merge does not contribute to hash_merge working.
    print("Using sort:    ", intersection_by_sort_and_merge(list(list_a), list(list_b)))
    print("Using hash set:", intersection_by_hash_set(list_a, list_b))
    return


def intersection_by_sort_and_merge(list_a, list_b):
    # Sort both lists first
    list_a.sort()
    list_b.sort()

    # Now find the intersection of the two sorted lists
    # (the elements that are in both lists).
    # The idea is that as long as the first elements from the two lists
    # are different from each other, the smallest element does not exist
    # in the other list, so we can skip over it. Only when we find the two
    # elements at the "front" (indicated by `a` and `b`) to be equal do we
    # add them to the result.
    # Using a list for `result` will cause elements to appear as many times
    # as the smallest number of appearances in either list; using a set will
    # cause each element to appear only once (the task did not say clearly
    # what should be done).
    # Notice how similar this is to the merge step in mergesort.
    result = set()
    a = b = 0
    while a < len(list_a) and b < len(list_b):
        if list_a[a] < list_b[b]:
            a += 1
        elif list_a[a] > list_b[b]:
            b += 1
        else:
            result.add(list_a[a])
            a += 1
            b += 1

    return list(result)


def intersection_by_hash_set(list_a, list_b):
    # Using a hash set for `set_a` is necessary for fast lookups.
    # In this approach to finding the intersection, it is also necessary
    # to use a hash set for `result` (and thus getting only unique results);
    # using a list would cause # elements to appear as many times as they
    # appear in `list_b` but not as many times as they appear in `list_a`.
    set_a = set(list_a)
    result = set()
    for item in list_b:
        if item in set_a:
            result.add(item)
    return list(result)


if __name__ == "__main__":
    main()
