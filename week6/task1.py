import os
import time
from random import shuffle, randrange
import sys

FILE_PATH = "testfile.bin"

# Block sizes to test, in bytes
BLOCK_SIZES = [8192, 4096, 2048, 1024, 512, 256, 128]

# File size is 256 MB, to avoid cache effects
FILE_SIZE = 256 * 1024 * 1024


def create_test_file():
    if os.path.exists(FILE_PATH):
        return

    print("Creating test file...")
    with open(FILE_PATH, "wb") as f:
        f.write(os.urandom(FILE_SIZE))
    print("Test file created.")


def sequential_read(block_size):
    start = time.perf_counter()
    with open(FILE_PATH, "rb") as f:
        # Read through the file sequentially in blocks until the end
        while f.read(block_size):
            pass
    end = time.perf_counter()
    return end - start


def random_read(block_size):
    file_size = os.path.getsize(FILE_PATH)
    batch_positions = list(range(0, file_size, block_size))
    shuffle(batch_positions)

    start = time.perf_counter()
    with open(FILE_PATH, "rb") as f:
        for pos in batch_positions:
            f.seek(pos)
            f.read(block_size)
    end = time.perf_counter()
    return end - start


def main():
    create_test_file()

    print(f"File size: {FILE_SIZE // (1024 * 1024)} MB\n")

    for block_size in BLOCK_SIZES:
        seq_time = sequential_read(block_size)
        rand_time = random_read(block_size)

        print(
            f"Block Size: {block_size:1} -> Sequential: {seq_time:.4f} (s) and Random: {rand_time:.4f} (s)"
        )

    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)


if __name__ == "__main__":
    main()
