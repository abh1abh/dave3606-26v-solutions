from os import listdir, path


def count_files_dfs(current_path, file_counts):
    is_file = path.isfile(current_path)
    is_directory = not is_file

    # If it's a file, update the count for its filename.
    if is_file:
        filename = path.basename(current_path)
        file_counts[filename] = file_counts.get(filename, 0) + 1

    # If it's a directory, find its children.
    # (In order for the loop to work, we must always have *a* list of
    # children, but for a regular file, the list is empty.)
    children = []
    if is_directory:
        for child_name in listdir(current_path):
            children.append(path.join(current_path, child_name))

    # Recurse into each child.
    for child in children:
        count_files_dfs(child, file_counts)


file_counts = {}
# Start the DFS from the current directory (".")
count_files_dfs(".", file_counts)
print(f"Found {len(file_counts)} unique filenames:")
print()
for filename in sorted(file_counts.keys()):
    count = file_counts[filename]
    print(f"{filename} {count}")
