def main():
    # Exercise 1A:
    string_sample = "Their was once a brave student"
    char_count = count_characters(string_sample)
    print("Character counts:", char_count)


def count_characters(string_sample):
    char_count = {}
    for char in string_sample:  # n iterations
        char = char.lower()  # 1 each time, n total
        if "a" <= char <= "z":  # 1 each time, n total
            if char in char_count:  # 1 each time, n total
                char_count[char] += 1  # 1 each time, n total
            else:
                char_count[char] = 1  # 1 each time, n total
    return char_count

    # Exercise 1B:
    # Time complexity analysis:
    # The loop runs n times.
    # Each operation inside the loop, checking and updating the dictionary, is O(1).
    # Overall time complexity is O(n).


if __name__ == "__main__":
    main()
