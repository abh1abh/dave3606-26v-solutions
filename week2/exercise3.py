from random import randint


def main():
    sample_values = [randint(0, 99) for _ in range(100)]  # Create 100 random integers.
    print("Original values:", sample_values)
    merge_sort(sample_values)
    print("Sorted values:  ", sample_values)


# Perform merge sort, writing the result back into the parameter list (instead of returning a new list).
def merge_sort(values):
    if len(values) <= 1:
        return

    # The operator // performs integer division, which will round the result down to
    # the nearest integer that is smaller than or equal to the actual quotient.
    middle = len(values) // 2
    # Split the list into two halves. The [:] operation is called "slicing",
    # and creates a copy of a part of the list. This means that we can now modify `values`
    # without losing the original numbers, which have been copied into `left` and `right`.
    left = values[:middle]
    right = values[middle:]

    # Recursion!
    merge_sort(left)
    merge_sort(right)

    # It's often nice for readability to have very short names for loop variables,
    # but when there are many such variables, it can be easy to forget what each variable means,
    # so can be good to use a letter that indicates which list it is an index for.
    # However, the letter `l` is a bad choice for a variable name, since it looks so much like the number 1.
    # So we add `i` (for "index") to each variable here.
    # `li`: The first index in `left` that we haven't merged yet.
    # `ri`: The first index in `right` that we haven't merged yet.
    # `vi`: The index in `values` where the next merged value will go.
    # Think of `li` and `ri` as the beginning of the parts of `left` and `right` that we haven't merged yet.
    li = ri = vi = 0

    # As long as there still are values in both `left` and `right`, we compare the "fronts" of the two lists,
    # and always pick the smallest one. Note that we're overwriting what was originally in `values`.
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            values[vi] = left[li]
            li += 1
        else:
            values[vi] = right[ri]
            ri += 1
        vi += 1

    # Now, one of the sides is empty, so we just copy over everything that remains in the other list.
    # One of these `while` loops will do nothing.
    while li < len(left):
        values[vi] = left[li]
        li += 1
        vi += 1

    while ri < len(right):
        values[vi] = right[ri]
        ri += 1
        vi += 1


if __name__ == "__main__":
    main()


"""
Analysis: Most lines are constant-time, except the slicing (total time n) and the recursive calls.
The three loops will run a total of n iterations (one per element that is copied into `values`).
Therefore, *except* for the recursive call, a single call to `merge_sort` with a list containing m elements
will take Θ(m) time. Since the recursion tree of merge sort is perfectly balanced, it contains lg n levels,
and level d of the tree will contain 2^d lists with n / 2^d elements in each, so the work performed at each level
is 2^d * Θ(n / 2^d) = Θ(n). Since there are lg n levels, the total complexity is Θ(n lg n).
"""
