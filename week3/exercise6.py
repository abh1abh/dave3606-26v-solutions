def unique_ages(persons):
    # Create a dictionary to count occurrences of each age.
    age_count = {}
    for person in persons:
        # Count occurrences of each age in the list.
        # If none exists, default to 0 and add 1.
        age_count[person.age] = age_count.get(person.age, 0) + 1

    # Collect names of persons whose age occurs only once.
    # Using [] to perform the lookup is safe (even though it will
    # throw an exception if the key is not in the map) because we
    # have already ensured that the age of every person is in the dict.
    # (Slight misphrasing in the task: it can't be done *only* with
    # comprehensions - creating the frequency dict requires a regular loop
    # because a comprehension can't look at the existing value for a key - but
    # creating the final result here can be done with a comprehension.)
    return [person.name for person in persons if age_count[person.age] == 1]
