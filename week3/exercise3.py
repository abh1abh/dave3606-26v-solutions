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
    return (x * x for x in values if x % 2 == 0)
    # Here we return a generator expression instead of a list.
    # This means that the squares of the even numbers are not computed
    # all at once, but rather one at a time as the code that uses the result reads from the generator.


# Exercise 1C:
# Time complexity analysis
# Both the list comprehension and the regular loop have a time complexity of Θ(n),
# where n is the number of elements in the input list values (since the condition and the
# transformation are constant-time operations).
# Because the generator comprehension does not create the entire list of results at once,
# the complexity of the generator expression itself is Θ(1), and if the code that calls it
# reads m elements from the generator, the complexity is Θ(m). Since m <= n (it's not possible
# to read more elements than there are in the list that the generator expression is based on),
# the complexity is also O(n). If you know that all elements will be read, the complexity is Θ(n).


if __name__ == "__main__":
    main()
