def main():
    list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_b = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    print("Using sort:", intersection_sort_merge(list_a, list_b))
    print("Using hash a set:", hash_merge(list_a, list_b))
    return


def intersection_sort_merge(list1, list2):
    # Sort both lists first
    list1.sort()
    list2.sort()

    # Now find the intersection of the two sorted lists
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            i += 1
        elif list1[i] > list2[j]:
            j += 1
        else:
            result.append(list1[i])
            i += 1
            j += 1

    return result


def hash_merge(list1, list2):
    set_a = set(list1)
    result = []
    for item in list2:
        if item in set_a:
            result.append(item)
    return result


if __name__ == "__main__":
    main()
