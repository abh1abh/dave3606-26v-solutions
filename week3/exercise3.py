def main():
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Exercise 1A result:", exercise1A(sample_values))
    print("Exercise 1B result:", list(exercise1B(sample_values)))


def exercise1A(values):
    result = []
    for x in values:
        if x % 2 == 0:
            result.append(x * x)
    return result


def exercise1B(values):
    result = (x * x for x in values if x % 2 == 0)
    return result
    # Here we return a generator expression instead of a list.
    # This means that the squares of the even numbers are not computed
    # all at once, but rather one at a time as they are needed.


# Exercise 1C:
# Time complexity analysis
# Both the list comprehension, regular loop  generator comprehension have a time complexity of O(n),
# where n is the number of elements in the input list values.
# However, the generator comprehension does not create the entire list of results at once.


if __name__ == "__main__":
    main()
