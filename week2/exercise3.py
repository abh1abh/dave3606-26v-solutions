def main():
    sample_array = [64, 25, 12, 22, 11]
    print("Original array is:", sample_array)
    merge_sort(sample_array)
    print("Sorted array is:", sample_array)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # // divides and floors the result
        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


if __name__ == "__main__":
    main()
