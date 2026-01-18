def unique_ages(persons):
    # Create a dictionary to count occurrences of each age.
    age_count = {}
    for person in persons:
        # Count occurrences of each age in the list.
        # If none exists, default to 0 and add 1.
        age_count[person.age] = age_count.get(person.age, 0) + 1

    # Collect names of persons whose age occurs only once.
    result = []
    for person in persons:
        # Check if the age occurs only once.
        if age_count[person.age] == 1:
            result.append(person.name)
    return result
